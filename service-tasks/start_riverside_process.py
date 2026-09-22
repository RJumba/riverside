from camunda_orchestration_sdk import (
    CamundaClient,
    MessagePublicationRequest,
    MessagePublicationRequestVariables,
)


def main():
    variables = MessagePublicationRequestVariables.from_dict(
        {
            "testScenario": "TC07",
            "referralReference": "TC07-REF-001",
        }
    )

    with CamundaClient() as client:
        result = client.publish_message(
            data=MessagePublicationRequest(
                name="gp-referral-received",
                correlation_key="TC07-REF-001",
                time_to_live=60000,
                variables=variables,
            )
        )

        print("--------------------------------")
        print("RIVERSIDE PROCESS START MESSAGE")
        print("--------------------------------")
        print("GP referral message published successfully.")
        print("Message: gp-referral-received")
        print("Correlation key: TC07-REF-001")
        print("Test scenario: TC07")
        print(f"Message key: {result.message_key}")
        print("--------------------------------")


if __name__ == "__main__":
    main()