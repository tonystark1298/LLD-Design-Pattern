
class Splitwise():
    def __init__(self) -> None:
        
        operation_type=input("Choose which operation you want to perform:\n1. Register User\n2. De-register user\n3. Make a group\n4. Add Expense\n5. Balance check\n6. Close the app\n")
        op_typ=[1,2,3,4,5]
        try:
            while int(operation_type) in op_typ:
                if operation_type=="1":
                    no_user=int(input("Enter the no of user to Register\n"))
                    for i in range(no_user):
                        user_id=input(f"Enter {i+1} User Id\n")
                        user_phone=input(f"Enter {i+1} Phone No\n")
                        if UserUpdate().isExistUser(user_id):
                            print("This user is already registered\n")
                        else:
                            UserUpdate().register_user(user_id,user_phone)
                
                elif operation_type=="2":
                    no_user=int(input("Enter the no of user to De-Register\n"))
                    for i in range(no_user):
                        user_id=input(f"Enter {i+1} User Id\n")
                        user_phone=input(f"Enter {i+1} Phone No\n")
                        if not UserUpdate().isExistUser(user_id):
                            print("This user is not registered\n")
                        else:
                            UserUpdate().delete_user(user_id,user_phone)

                elif operation_type =="3":
                    #Makes a group and if a participant is not register then it register it also
                
                    group_name=input("Enter the group name\n")
                    if MakeGroup(group_name).isExistGroup():
                        print("Group name exist")
                    else:
                        MakeGroup(group_name).registerGroup()
                        group_count=input("Enter the no of people in group:\n")
                        for i in range (int(group_count)):
                            user_id=input(f"Enter the user_id of {i+1}:\n")
                            MakeGroup(group_name).add_participant(user_id)

                elif operation_type=="4":
                    #ADD Expense of a group
                    group_name=input("Enter the Group-name:\n")
                    filter=True
                    if not MakeGroup(group_name).isExistGroup():
                        filter=False
                        print("Group doesn't exist")
                    if filter:
                        spendor_id=input("Enter the Spendor's id:\n")
                    if filter and not UserUpdate().isExistUser(spendor_id):
                        filter=False
                        print("User is not registered")
                    if filter and spendor_id not in MakeGroup(group_name).group_dict[group_name]:
                        filter=False
                        print("User is not part of group")
                    if filter:    
                        amount=int(input("Enter the Amount:\n"))
                        currency=input('''Enter the type of currency as "Dollor" or "Inr":\n''')
                        type=input('''Enter the type of distribution as "Equal", "Unequal", "Percent":\n''')
                        functions={"dollorequal":DollorExpense(spendor_id, group_name, amount).equal, 
                            "dollorunequal":DollorExpense(spendor_id, group_name, amount).unequal_with_values, 
                            "dollorpercent":DollorExpense(spendor_id, group_name, amount).unequal_with_percent,
                            "inrequal":AddExpense(spendor_id, group_name, amount).equal, 
                            "inrunequal":AddExpense(spendor_id, group_name, amount).unequal_with_values, 
                            "inrpercent":AddExpense(spendor_id, group_name, amount).unequal_with_percent,
                            }
                        try:
                            functions[currency.lower()+type.lower()]()
                        except:
                            print("Enter the currency and type of transaction properly")
        
                else:
                    #Display the Balance of Users
                    user_id=input("Enter the user id to check balance\n")
                    if UserUpdate().isExistUser(user_id):
                        UserUpdate().show_balance(user_id)
                        if MakeGroup.user_group.get(user_id) is None:
                            print("User is not part of any group")
                        else:
                            print("User is part of groups: ",MakeGroup.user_group[user_id])
                            group_name=input("Enter the group name to see balance of all members of group\n")
                            if MakeGroup.group_dict.get(group_name) is None or not user_id in MakeGroup.group_dict[group_name]:
                                group_name=input("Enter a valid group name or user id") 
                            else:
                                for member in MakeGroup.group_dict[group_name]:
                                    UserUpdate().show_balance(member)
                    else:
                        print("Invalid User")
                    
                operation_type=input("Choose which operation you want to perform:\n1. Register User\n2. De-register user\n3. Make a group\n4. Add Expense\n5. Balance check\n6. Close the app\n")
        except:
            print("Enter valid operation")
            Splitwise()
        print("It's sad that you are leaving :(\n")

class UserUpdate():
    user_dict={}
    user_balance={}
    def __init__(self) -> None:
        pass
    
    def register_user(self,user_id,phone):
        self.user_dict[user_id]=phone
        self.user_balance[user_id]=0

    def delete_user(self,user_id,phone):
        del self.user_dict[user_id]
        print(f"your balance is {self.user_balance[user_id]}")
        self.user_balance[user_id]
    
    def show_balance(self,user_id):
        print(f"User with Id: {user_id} has balance Rs: {self.user_balance[user_id]}\nyour balance in Dollar: {self.user_balance[user_id]/83}")
    
    def isExistUser(self,user_id):
        if self.user_dict.get(user_id) is None:
            return False
        return True

class MakeGroup():
    group_dict={}
    user_group={}
    def __init__(self,groupname) -> None:
        self.groupname=groupname

    def add_participant(self,user_id):
        info=UserUpdate
        if info.user_dict.get(user_id) is not None:
            self.group_dict[self.groupname].append(user_id)
            if user_id in self.user_group:
                self.user_group[user_id].append(self.groupname)
            else:
                self.user_group[user_id]=[]
                self.user_group[user_id].append(self.groupname)
        else:
            print(f"Person with id {user_id} is not registered\n")    
    
    def registerGroup(self):
        self.group_dict[self.groupname]=[]

    def isExistGroup(self):
        if self.group_dict.get(self.groupname) is None:
            return False
        return True

class AddExpense():
    def __init__(self,spender_id, groupname, amount_spent) -> None:
        self.spender_id=spender_id
        self.amount_spent=int(amount_spent)
        self.groupname=groupname
        self.info=UserUpdate
        self.group=MakeGroup.group_dict[self.groupname]

    def equal(self):
        self.info.user_balance[self.spender_id]+=self.amount_spent
        for member in self.group:
            self.info.user_balance[member]-=self.amount_spent/len(self.group)
    
    def unequal_with_percent(self):
        percent=0
        user_percent={}
        for member in self.group:
            print(f"Enter the percent expense of {member}\n")
            percent_person=int(input())
            percent+=percent_person
            user_percent[member]=percent_person
        if percent==100:
            self.info.user_balance[self.spender_id]+=self.amount_spent
            for member in self.group:
                self.info.user_balance[member]-=self.amount_spent*(user_percent[member]/100)
        else:
            print("Sum of percentage is not equal to 100 try again")

    def unequal_with_values(self):
        individual_sum=0
        individual_amount={}
        for member in self.group:
            print(f"Enter the expense of {member}\n")
            person_spent=int(input())
            individual_sum+=person_spent
            individual_amount[member]=person_spent
        if individual_sum==self.amount_spent:
            self.info.user_balance[self.spender_id]+=self.amount_spent
            for member in self.group:
                self.info.user_balance[member]-=individual_amount[member]
        else:
            print("Sum of individual spent is not equal to Total spent try again")
       
class DollorExpense(AddExpense):
    def __init__(self, spender_id, groupname, amount_spent) -> None:
        super().__init__(spender_id, groupname, amount_spent)

    def equal(self):
        self.info.user_balance[self.spender_id]+=80*self.amount_spent
        for member in self.group:
            self.info.user_dict[member]-=80*self.amount_spent/len(self.group)

    def unequal_with_percent(self):
        for member in self.group:
            self.info.user_balance[self.spender_id]+=80*self.amount_spent
            print(f"Enter the percent expense of {member}\n")
            percent_person=int(input())
            self.info.user_balance[member]-=80*self.amount_spent*(percent_person/100)
    
    def unequal_with_values(self):
        for member in self.group:
            self.info.user_balance[self.spender_id]+=80*self.amount_spent
            print(f"Enter the expense of {member}\n")
            percent_person=int(input())
            self.info.user_balance[member]-=80*self.amount_spent

if __name__=="__main__":
    Splitwise()

