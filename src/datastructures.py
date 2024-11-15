
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)



    def add_member(self, member):
        # fill this method and update the return
        member["id"] = self._generateId()
        self._members.append(member)

    
    def update_member(self, id, update_data):
        for memb in self._members:
            if memb.get('id') == id:
                for key, value in update_data.items():  
                    memb[key] = value             
                return memb                      
        return None 
                

     

    def replace_member(self, id, new_menb):
        for y in self._members:
            if y.get('id') == id:
                y = new_menb












    def delete_member(self, id):
        # fill this method and update the return
        for x in range(len(self._members)):
            if self._members[x]["id"] == id:       
                self._members.pop(x)






    

    def get_member(self, id):
        # fill this method and update the return
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:       
                return self._members[i] 





    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
