class NIDManager:
    def __init__(self):
        self.nid_numbers = []

    def add_nid(self, nid):
        self.nid_numbers.append(nid)

    def display_nids(self):
        print("List of NID Numbers:")
        for nid in self.nid_numbers:
            print(nid)

    def delete_nid(self, nid):
        if nid in self.nid_numbers:
            self.nid_numbers.remove(nid)
            print("NID Number", nid, "has been deleted.")
        else:
            print("NID Number", nid, "not found.")

    def update_nid(self, old_nid, new_nid):
        if old_nid in self.nid_numbers:
            index = self.nid_numbers.index(old_nid)
            self.nid_numbers[index] = new_nid
            print("NID Number", old_nid, "has been updated to", new_nid)
        else:
            print("NID Number", old_nid, "not found.")

# Example usage:
nid_manager = NIDManager()

# Adding NID Numbers
nid_manager.add_nid("123456789")
nid_manager.add_nid("987654321")

# Displaying NID Numbers
nid_manager.display_nids()

# Deleting NID Numbers
nid_manager.delete_nid("123456789")

# Updating NID Number
nid_manager.update_nid("987654321", "111111111")

# Displaying NID Numbers after operations
nid_manager.display_nids()
