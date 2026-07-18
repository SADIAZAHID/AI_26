import re

# Your raw text data
text = """[Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
ullamco laboris nisi ut aliquip ex ea commodo consequat. testuser_01@example.com 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu 
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum. Curabitur pretium 
tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, 
est eros bibendum elit, nec luctus magna felis sollicitudin mauris. contact_me@testmail.org 
Integer imperdiet lectus quis justo. Integer in sem. Duis leo. Sed fringilla mauris sit amet 
nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit 
cursus nunc, quis gravida magna mi a libero. Fusce dui leo, imperdiet in, sit amet, 
sales@provider.com commodo at, pretium nec, metus. Mauris tincidunt felis sed dolor.
 Aliquam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper 
 libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus
  pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus.
employee_data@sample.net Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante.
Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh.
Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, 
 quis gravida magna mi a libero. Fusce dui leo, imperdiet in, sit amet, marketing@provider.com 
 commodo at, pretium nec, metus. Mauris tincidunt felis sed dolor. Aliquam rhoncus. Maecenas 
tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque
sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio
 et ante tincidunt tempus. hr_dept@example.com Donec vitae sapien ut libero venenatis faucibus. 
 Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla 
mauris sit amet nibh. support@testmail.org Donec sodales sagittis magna. Sed consequat, leo
 eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce dui leo,
 imperdiet in, sit amet, commodo at, pretium nec, metus. info@sample.net Mauris tincidunt felis 
sed dolor. Aliquam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper
 libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar,
 hendrerit id, lorem. user_alpha@provider.com Maecenas nec odio et ante tincidunt tempus. 
 Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci
 eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales 
 sagittis magna. Sed consequat, leo eget bibendum sodales, auguewebmaster@example.com 
 velit cursus nunc, quis gravida magna mi a libero. Fusce dui leo, imperdiet in, sit amet,
commodo at, pretium nec, metus. Mauris tincidunt felis sed dolor. Aliquam rhoncus. 
feedback@testmail.org Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, 
sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, 
lorem. Maecenas nec odio et ante tincidunt tempus. newsletter@sample.net Donec vitae sapien ut libero 
venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed 
fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, 
admin@provider.com augue velit cursus nunc, quis gravida magna mi a libero. Fusce dui leo, imperdiet in, 
sit amet, commodo at, pretium nec, metus. Mauris tincidunt felis sed dolor. Aliquam rhoncus. Maecenas 
tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum.
account_support@example.com Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. 
ante.gittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna 
mi a libero. Fusce dui leo, imperdiet in, sit amet, commodo at, query@provider.com pretium nec, metus. 
Mauris tincidunt felis sed dolor. Aliquam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem 
quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, 
hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. secure_inbox@example.com Donec .]"""


# The regex pattern for a standard email
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all matches and save to a list
mails = re.findall(email_pattern, text)

# Print the list and the total count
print(f"Found {len(mails)} emails:")
print(mails)