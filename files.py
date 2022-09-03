# # import os
# # comments = "# Start of a new Python program"

# # file = open ("merouane.py", 'w')
# # f = os.path.getsize('merouane.py')
# # print(f)
# # # file.write(comments)

import os ,re ,sys
# # def create_python_script(filename):
# #   comments = "# Start of a new Python program"
# #   with open(filename , 'a') as f:
# #     filesize = f.write(comments)
# #   return(filesize)

# # print(create_python_script("program.py"))


# #!/usr/bin/env python3

# def read_employees(csv_file_location):
#         csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
#         employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
#         employee_list = []
#         for data in employee_file:
#               employee_list.append(data)
#         return employee_list

# employee_list = read_employees("/home/student-01-48fec289689b/scripts/employees.csv" )
# print(employee_list)



# def read_employees(csv_file_location):
#    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
#    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
#    employee_list = []
#    for data in employee_file:
#       employee_list.append(data)
#    return employee_list
# employee_list = read_employees('/home/student-00-807b64735878/data/employees.csv')
# print(employee_list)                     

# import csv

# def contains_domain(address, domain):
#       domain_pattern = r'[\w\.-]+@'+domain+'$'
#       if re.match(domain_pattern, address):
#            return True
#       return False
    
# def replace_domain(address, old_domain, new_domain):
#       old_domain_pattern = r'' + old_domain + '$'
#       address = re.sub(old_domain_pattern, new_domain, address)
#       return address   
#     /home/student-01-6fa7c5457845/scripts/user_emails.csv
    
    
# #!/usr/bin/env python3import sys
# import csv
# def populate_dictionary(filename):
#   """Populate a dictionary with name/email pairs for easy lookup."""
#   email_dict = {}
#   with open(filename) as csvfile:
#     lines = csv.reader(csvfile, delimiter = ',')
#     for row in lines:
#       name = str(row[0].lower())
#       email_dict[name] = row[1]
#   return email_dict
# def find_email(argv):
#   """ Return an email address based on the username given."""
#   # Create the username based on the command line input.
#   try:
#     fullname = str(argv[1] + " " + argv[2])
#     # Preprocess the data
#     email_dict = populate_dictionary('/home/student-01-f8f8cbc50c6c/data/user_emails.csv')
#     # Find and print the email
#     return email_dict.get(fullname.lower())
#   except IndexError:
#     return "Missing parameters"
# def main():
#   print(find_email(sys.argv))
# if __name__ == "__main__":
#   main()
  
#   #!/usr/bin/env python3
# import sys
# import csv
# def populate_dictionary(filename):
#   """Populate a dictionary with name/email pairs for easy lookup."""
#   email_dict = {}
#   with open(filename) as csvfile:
#     lines = csv.reader(csvfile, delimiter = ',')
#     for row in lines:
#       name = str(row[0].lower())
#       email_dict[name] = row[1]
#   return email_dict
# def find_email(argv):
#   """ Return an email address based on the username given."""
#   # Create the username based on the command line input.
#   try:
#     fullname = str(argv[1] + " " + argv[2])
#     # Preprocess the data
#     email_dict = populate_dictionary('/home/{{ username }}/data/user_emails.csv')
#     # Find and print the email
#     return email_dict.get(fullname.lower())
#   except IndexError:
#     return "Missing parameters"
# def main():
#   print(find_email(sys.argv))
# if __name__ == "__main__":
#   main()
  
# #!/usr/bin/env python3
# import sys
# import csv
# def populate_dictionary(filename):
#   """Populate a dictionary with name/email pairs for easy lookup."""
#   email_dict = {}
#   with open(filename) as csvfile:
#     lines = csv.reader(csvfile, delimiter = ',')
#     for row in lines:
#       name = str(row[0].lower())
#       email_dict[name] = row[1]
#   return email_dict
# def find_email(argv):
#   """ Return an email address based on the username given."""
#   # Create the username based on the command line input.
#   try:
#     fullname = str(argv[1] + " " + argv[2])
#     # Preprocess the data
#     email_dict = populate_dictionary('/home/student-01-f8f8cbc50c6c/data/user_emails.csv')
#     # Find and print the email
#     return email_dict.get(fullname.lower())
#   except IndexError:
#     return "Missing parameters"
# def main():
#   print(find_email(sys.argv))
# if __name__ == "__main__":
#   main()  
  
  
#   #!/usr/bin/env python3
# import csv
# import sys
# def populate_dictionary(filename):
#   """Populate a dictionary with name/email pairs for easy lookup."""
#   email_dict = {}
#   with open(filename) as csvfile:
#     lines = csv.reader(csvfile, delimiter = ',')
#     for row in lines:
#       name = str(row[0].lower())
#       email_dict[name] = row[1]
#   return email_dict
# def find_email(argv):
#   """ Return an email address based on the username given."""
#   # Create the username based on the command line input.
#   try:
#     fullname = str(argv[1] + " " + argv[2])
#     # Preprocess the data
#     email_dict = populate_dictionary('/home/student-01-f8f8cbc50c6c/data/user_emails.csv')
#      # If email exists, print it
#     if email_dict.get(fullname.lower()):
#       return email_dict.get(fullname.lower())
#     else:
#       return "No email address found"
#   except IndexError:
#     return "Missing parameters"
# def main():
#   print(find_email(sys.argv))
# if __name__ == "__main__":
#   main()
#   #======   
#   #week 2 assingment coursera python course
  
#   import subprocess
# from multiprocessing import Pool
# import os


# def backup(src):
#     dest = os.getcwd() + "/data/prod_backup/"
#     print("Backing up {} into {}".format(src, dest))
#     subprocess.call(["rsync", "-arq", src, dest])


# if _name_ == "__main__":
#     src = os.getcwd() + "/data/prod/"
#     list_of_files = os.listdir(src)
#     all_files = []

#     for value in list_of_files:
#         full_path = os.path.join(src, value)
#         all_files.append(full_path)

#     with Pool(len(all_files)) as pool:
#         pool.map(backup, all_files)

    
import operator     
error ={}
user ={}
f = open ("C:\\Users\\Meoruane\\Desktop\\error_message.csv","r")
for line in f.readlines(): 
      inter = line.strip()
      inter2 = re.search(r"ticky: ERROR ([\w' ]*) ", inter)
      inter_user= re.search(r" \(([\w.]*)\)",inter)
      #print(inter_user[1])
      if inter_user[1] not in user.keys():
            user[inter_user[1]]=1
      else:
            user[inter_user[1]]=user[inter_user[1]] + 1      
      if inter2[1] not in error.keys():
            error[inter2[1]]=1
      else:
            error[inter2[1]]=error[inter2[1]] + 1            
     
f.close()   
#sort the dictionary 
list = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
#print(list)
print(user)
f1 = open ("C:\\Users\\Meoruane\\Desktop\\error_message2.csv","w")
f1.write('Error, Count')
f1.write('\n')
i=0
while i< len(list):
      f1.write('{}, {}'.format(list[i][0],list[i][1]))
      f1.write('\n')
      i=i+1
f1.close

#Second Part of programme