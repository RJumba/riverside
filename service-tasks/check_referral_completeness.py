import asyncio

from camunda_orchestration_sdk import (
    CamundaAsyncClient,
    ConnectedJobContext,
    WorkerConfig,
)


async def check_referral_completeness(
    job: ConnectedJobContext,
) -> dict[str, object]:

    variables = job.variables.to_dict()

    print("\n--------------------------------")
    print("CHECK REFERRAL COMPLETENESS")
    print("--------------------------------")
    print("Received variables:")
    print(variables)

    result = {
        "referralComplete": True,
        "referralCheckMessage": "Referral completeness check successful",
    }

    print("Returning to Camunda:")
    print(result)
    print("--------------------------------\n")

    return result


async def main() -> None:

    async with CamundaAsyncClient() as client:

        worker_config = WorkerConfig(
            job_type="check-referral-completeness",
            job_timeout_milliseconds=30_000,
        )

        client.create_job_worker(
            config=worker_config,
            callback=check_referral_completeness,
        )

        print("Riverside worker is running.")
        print("Waiting for: check-referral-completeness")
        print("Press Ctrl+C to stop the worker.\n")

        await client.run_workers()


if __name__ == "__main__":
    asyncio.run(main())