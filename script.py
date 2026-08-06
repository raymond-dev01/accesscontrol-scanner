# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

rev_badges = {'X1111','C2222','Z3333','F4444'}
approved = []
denied = []

while True:
    visitor_name = input('Enter your name: ')
    
    if visitor_name.lower() == 'done':
        break
    
    ask_badge = input('What is your badge number? ').strip().upper()
    
    if ask_badge in rev_badges:
        denied.append(visitor_name)
        print('ACCESS DENIED')
        
    
    else:
        ask_badge not in rev_badges
        approved.append(visitor_name)
        print('ACCESS GRANTED')
        

approved.sort()
denied.sort()
  
print('=====ACCESS SUMMARY=====')
print(":white_check_mark: Approved Visitors") 
for person in sorted(approved):
  print(f" - {person}")

print("⛔️ Denied Visitors")
for person in sorted(denied):
  print(f" - {person}")

print(f'The total number of approved visitors are: {len(approved)}')
print(f'The total number of denied visitors are: {len(denied)}')


#Source Control Testing in VS Code
print("This is a test for source control in VS Code")
