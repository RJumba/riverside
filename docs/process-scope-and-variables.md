Riverside Hospital Process Scope

## Process Start
GP referral is received by the Riverside Hospital specialist unit.

## Process End
The final outcome is communicated to both the patient and the GP.





Actors / Participants

- GP Practice
- Patient
- Patient Booking Team
- Specialist Doctor
- Laboratory Team
- Medical Secretary
- Camunda Workflow System






So before I start the process of drawing my very own bpmn i have to take note of the processes that are happening in the hospital. The processes that are happening in the hospital are as follows:

1. GP sends a referral to Riverside Hospital.
2. The hospital receives the referral.
3. Referral information is checked.
4. If information is missing, clarification is requested from the GP.
5. Once complete, an initial consultation is arranged.
6. The patient is informed of the appointment.
7. The Specialist Doctor conducts the consultation.
8. The doctor decides the next action.
9. The patient may require discharge, follow-up, laboratory testing or treatment.
10. If laboratory testing is required, the laboratory performs the test and the doctor reviews the results.
11. The final outcome is prepared.
12. The outcome is communicated to the patient and GP.




The following are the main decisions that should be considered in the process:

- Is the referral complete?
- What is the consultation outcome?
- Are laboratory tests required?
- Have laboratory results been received?
- Is the final communication ready to send?





The process variables that would be required throughout the process are as follows:

patientName
nhsNumber
dateOfBirth
contactDetails
referringGP
gpPractice
referralReason
referralPriority

referralComplete
missingFields

appointmentDate
appointmentType
appointmentReference

consultationNotes
consultationOutcome

labRequired
labAppointmentDate
labResult

finalDecision
draftPatientLetter
draftGPLetter
letterApproved
letterSent