# Riverside Hospital Process Scope

## Process Start
GP referral is received by the Riverside Hospital specialist unit.

## Process End
The final outcome is communicated to both the patient and the GP.





# Actors / Participants

- GP Practice
- Patient
- Patient Booking Team
- Specialist Doctor
- Laboratory Team
- Medical Secretary
- Camunda Workflow System




## High-Level Process


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




## Main Process Decisions

- Is the referral complete?
- What is the consultation outcome?
- Are laboratory tests required?
- Have laboratory results been received?
- Is the final communication ready to send?





## Process Variables

### Referral Information

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

## Human Activities

- Receive and record referral
- Review missing referral information
- Request clarification from GP Practice
- Schedule consultation
- Record consultation notes
- Record consultation outcome
- Perform laboratory tests
- Review laboratory results
- Review final communication
- Confirm communication has been sent


## Candidate Automated Activities

- Check referral information for completeness
- Generate appointment reference
- Generate draft outcome communication