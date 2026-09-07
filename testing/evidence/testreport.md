# Riverside Hospital Workflow Testing Report

## 1. Testing Objective

The purpose of testing was to confirm that the Riverside Hospital operational workflow works correctly in Camunda 8.

Testing focused on:

- Automated service tasks
- Python job workers
- Process variables
- Gateway decisions
- Camunda forms
- End-to-end process execution

---

## 2. Test Environment

- Camunda 8
- Camunda Modeler 5.49.0
- Camunda 8 Run (local)
- Camunda Operate
- Camunda Tasklist
- Python
- Camunda Python SDK
- Visual Studio Code

All test data used was fictional.

---

## 3. Test Cases

### Test ID: TC01

Scenario: Check referral completeness service task

Input:
Referral completeness worker test

Expected Result:
The service task should be picked up by the Python worker and
return referralComplete = true.

Actual Result:
The Camunda job was successfully created, the Python worker
picked up the job and returned referralComplete = true.

Status: PASS

Evidence:
TC01_check_referral_completeness_camunda.png
TC01_check_referral_completeness_worker.png

Defects:
None during this isolated worker test.

Limitation:
The initial TC01 test used a temporary fixed true result.
The final worker implementation was later updated to validate
the actual referral form fields and identify missing information.

---

### Test ID: TC02

Scenario: Generate appointment reference and confirmation service task

Input:
Appointment reference generation worker test

Expected Result:
The service task should be picked up by the Python worker and
generate a unique appointment reference and confirmation message.

Actual Result:
The Camunda job was successfully created, the Python worker
picked up the job and generated a unique appointment reference
and confirmation message.

Status: PASS

Evidence:
TC02_generate_appointment_reference_camunda.png
TC02_generate_appointment_reference_worker.png

Defects:
None during this test.

Limitation:
This test confirms successful appointment reference generation
but does not test delivery through an external patient
communication platform.

---

### Test ID: TC03

Scenario: Generate draft outcome letter service task

Input:
Draft outcome letter generation worker test using patient name,
final outcome type and consultation notes.

Expected Result:
The service task should be picked up by the Python worker and
generate a draft outcome letter using the supplied patient and
clinical outcome information.

Actual Result:
The Camunda job was successfully created, the Python worker
picked up the job and generated a draft outcome letter containing
the patient name, clinical outcome and consultation notes.

Status: PASS

Evidence:
TC03_generate_draft_outcome_letter_camunda.png
TC03_generate_draft_outcome_letter_worker.png

Defects:
None during the isolated service task test.

Limitation:
This test confirms automated draft generation but does not send
the communication to a real external GP or patient system.

---

### Test ID: TC04

Scenario:
End-to-end successful Riverside Hospital referral pathway

Input:
A complete fictional GP referral was submitted.

The process followed:

- Complete referral
- Routine consultation
- No laboratory investigation required
- Discharge back to GP as the final clinical outcome

Expected Result:
The workflow should accept the complete referral, pass through
the referral completeness gateway, schedule the consultation,
generate an appointment reference, complete the consultation,
follow the no-laboratory branch, record discharge as the final
outcome, generate the draft outcome communication and successfully
reach the end of the process.

Actual Result:
The Riverside Hospital workflow successfully processed the
referral from the GP referral message through to final outcome
communication.

The referral completeness check completed successfully and the
complete-referral branch was selected.

The consultation was scheduled and an appointment reference was
generated automatically.

The specialist consultation was completed and the process
successfully followed the no-laboratory pathway.

Discharge back to GP was selected as the final clinical outcome.

The draft outcome communication was generated, reviewed and
finalised.

The final outcome was sent to the patient and GP and the Camunda
process instance reached successful completion.

Status: PASS

Evidence:
Use the exact TC04 filenames stored in the testing/evidence folder,
including the final outcome, process history, completed process
and final process-variable screenshots.

Defects:
Several integration defects were identified during TC04 and
corrected during testing.

1. Gateway condition expressions initially contained duplicated
leading equals signs, which prevented BPMN deployment.

2. Some linked Camunda forms had not initially been deployed,
resulting in "Form not found" incidents.

3. Laboratory Test Required was initially implemented using a
Checkbox Group. This produced labRequired = [] instead of the
Boolean value required by the gateway.

4. The laboratory form component was changed to a single Checkbox,
allowing labRequired to return true or false correctly.

5. Draft outcome communication variable names did not initially
match between the Python worker and the outcome review form.

6. The worker output and form field bindings were aligned so that
the generated outcome communication could be reviewed correctly.

All identified issues were corrected and the same end-to-end
workflow was successfully completed.

Limitation:
The end-to-end workflow was tested locally using fictional data.
No real hospital, GP, laboratory, email or patient communication
systems were connected.

---

## 4. Overall Testing Result

TC01: PASS
TC02: PASS
TC03: PASS
TC04: PASS

All four main test scenarios completed successfully.

The testing demonstrated that:

- Camunda can communicate with the Python job workers.
- Referral information can be processed using workflow variables.
- Automated appointment references can be generated.
- Draft outcome communications can be generated.
- Gateway conditions correctly control process routing after
configuration issues were resolved.
- Camunda forms support the main human workflow activities.
- The Riverside Hospital process can execute successfully from
referral receipt through to final outcome communication.

---

## 5. Testing Limitations

The implementation was tested in a local Camunda 8 Run environment.

Fictional patient and GP information was used throughout testing.

External hospital systems, real GP systems, laboratory systems,
email services and patient notification platforms were outside
the scope of the prototype.

The testing therefore demonstrates the workflow logic and
automation behaviour rather than a production hospital
integration.

---

## 6. Conclusion

Testing confirmed that the Riverside Hospital workflow can be
executed successfully in Camunda 8.

The automated service tasks, forms, process variables, gateway
conditions and end-to-end business process were tested and
validated.

Defects discovered during integration testing were corrected and
the final end-to-end process completed successfully.