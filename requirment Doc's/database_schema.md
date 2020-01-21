# MODEL/DB FIELDS

### Company_Services
- service_id: INT
- service_name: STR
- description: TEXT
- service_had: STR
- contact: INT
- start_date: date

### Calibration_Services
- id: INT
- type: STR
- name: STR
- description: TEXT
- start_date: date


### Product
- id: INT
- realtor: INT (FOREIGN KEY [realtor])
- title: STR
- address: STR
- city: STR
- state: STR
- zipcode: STR
- description: TEXT
- price: INT
- bedrooms: INT
- bathrooms: INT
- garage: INT [0]
- sqft: INT
- lot_size: FLOAT
- is_published: BOOL [true]
- list_date: DATE
- photo_main: STR
- photo_1: STR
- photo_2: STR
- photo_3: STR
- photo_4: STR
- photo_5: STR
- photo_6: STR


### CONTACT
- branch_name: STR
- address: TEXT
- email: STR
- phone: INT
- mobile: INT
- contact_Person: STR

### ENQUIRY
- id: INT
- name: STR
- company: SRT
- email: STR
- phone: STR
- address/location: TEXT
- Product: INT
- Service: INT
- Requirements: TEXT
- Image: IMG
- File : doc
- enquiry_date: DATE