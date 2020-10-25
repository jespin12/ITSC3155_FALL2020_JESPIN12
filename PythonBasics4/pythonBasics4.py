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
    # YOUR CODE HERE
    if len(contact_info) == 0:
        return contacts
    else:
        y = 0
        x = 0

        for x in contacts.keys():
            contacts[x] = contact_info[[y][a]]
    return contacts

# # Part C.
def dict_2_array(contacts):
    # YOUR CODE HERE

    return

