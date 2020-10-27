# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.
def array_2_dict(emails, contacts):
    # YOUR CODE HERE
    contactName = list(contacts)
    for x in range(len(emails)):
        contacts[contactName[x]] = emails[x]
    return contacts

    

# # Part B.
def array2d_2_dict(contact_info, contacts):
    new_dictionary = {}
    if len(contact_info) == 0 or not any(contact_info):
        for x in contacts:
            new_dictionary[x] = ""
    else:
        for i in range(0,len(contact_info)):
            create_info = {}
            create_info['email'] = contact_info[i][0]
            create_info['phone'] = contact_info[i][1]
            new_dictionary[list(contacts)[i]] = create_info
    
    return new_dictionary


# # Part C.
def dict_2_array(contacts):
    # YOUR CODE HERE
    arr_name = []
    arr_email = []
    arr_phone = []
    if len(contacts) == 0:
        return [arr_name, arr_email, arr_phone]
    else: 
        for x in contacts:
            arr_name.append(x)
            arr = contacts[x]
            arr_email.append(arr["email"])
            arr_phone.append(arr["phone"])
    return [arr_email, arr_phone, arr_name]

