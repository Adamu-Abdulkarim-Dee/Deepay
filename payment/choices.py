#Used for Account status
ACCOUNT_STATUS = (
    ('ACTIVE', 'ACTIVE'),
    ('FREEZE', 'FREEZE'),
    ('CLOSED', 'CLOSED')
)

#Used for Transactional Status
STATUS = (
    ('SUCCESS(00)', 'SUCCESS(00)'),
    ('FAILED(01)', 'FAILED(01)'),
    ('REVERSED(02)', 'REVERSED(02)')
)

#Used for Complaint model
TYPE_OF_COMPLAINT = (
    ('Transactional', 'Transactional'),
    ('Non Transactional', 'Non Transactional'),
    ('Account Status', 'Account Status'),
    ('Feedback', 'Feedback'),
)
LANGUAGE = (
    ('English Language', 'English Language'),
    ('Hausa Language', 'Hausa Language')
)