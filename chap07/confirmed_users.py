# Start with users that need to be verified,
   #  and an empty list to hold confirmed users.
dumb = ['kayla', 'skye', 'inge']
schools = []
   # Verify each user until there are no more unconfirmed users.
   #  Move each verified user into the list of confirmed users.
while dumb:
    current = dumb.pop()
    print(f"Grading student {current.title()}")
    schools.append(current)
# Display all confirmed users.
print("\nThe following are smart now")
for school in schools:
    print(school.title())