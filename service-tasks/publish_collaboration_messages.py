import asyncio
from typing import Any

from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ConnectedJobContext,
    MessagePublicationRequest,
    MessagePublicationRequestVariables,
    WorkerConfig,
)

# Keep messages available long enough to survive small timing differences while testing.
MESSAGE_TTL_MS = 60 * 60 * 1000  # 1 hour


async def _publish_message(
    job: ConnectedJobContext,
    message_name: str,
) -> dict[str, Any]:
    variables = job.variables.to_dict()

    nhs_number = variables.get("nhsNumber")
    if nhs_number is None or str(nhs_number).strip() == "":
        raise ValueError(
            f"Cannot publish '{message_name}': process variable 'nhsNumber' is missing or blank."
        )

    correlation_key = str(nhs_number).strip()

    await job.client.publish_message(
        data=MessagePublicationRequest(
            name=message_name,
            correlation_key=correlation_key,
            time_to_live=MESSAGE_TTL_MS,
            variables=MessagePublicationRequestVariables.from_dict(variables),
        )
    )

    job.log.info(
        "Published BPMN message '%s' with nhsNumber='%s'",
        message_name,
        correlation_key,
    )

    return {
        "lastPublishedMessage": message_name,
        "lastMessageCorrelationKey": correlation_key,
    }


async def publish_gp_referral(job: ConnectedJobContext) -> dict[str, Any]:
    return await _publish_message(job, "gp-referral-received")


async def publish_clarification_request(job: ConnectedJobContext) -> dict[str, Any]:
    return await _publish_message(job, "referral-clarification-request")


async def publish_clarification_response(job: ConnectedJobContext) -> dict[str, Any]:
    return await _publish_message(job, "referral-clarification-response")


async def publish_final_clinical_outcome(job: ConnectedJobContext) -> dict[str, Any]:
    return await _publish_message(job, "final-clinical-outcome")


async def main() -> None:
    async with CamundaAsyncClient() as client:
        workers = [
            ("publish-gp-referral", publish_gp_referral),
            ("publish-referral-clarification-request", publish_clarification_request),
            ("publish-referral-clarification-response", publish_clarification_response),
            ("publish-final-clinical-outcome", publish_final_clinical_outcome),
        ]

        for job_type, callback in workers:
            client.create_job_worker(
                config=WorkerConfig(
                    job_type=job_type,
                    job_timeout_milliseconds=30_000,
                ),
                callback=callback,
            )

        print("Collaboration message worker is running.")
        print("Listening for:")
        for job_type, _ in workers:
            print(f"  - {job_type}")

        await client.run_workers()


if __name__ == "__main__":
    asyncio.run(main())
