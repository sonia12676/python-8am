# class Students:
#     s_list=['ram','shyam','hari']

#     def show(self):
#         for a in self.s_list:
#             print(a)

#     def add(self,name):
#         self.s_list.append(name)
#         # print(self.s_list)

#     def delete(self,index):
#         self.s_list.pop(index)
#         # print(self.s_list)

#     def update(self,index,name):
#         self.s_list[index]=name
#         print(self.s_list)

# std=Students()
# # std.show()
# std.add("tika")
# std.delete(2)
# std.update(0,"harry")


# __str__
# __repr__
# __add__
# what is setter and getter, static method and class method, class decorator , property decorator

# *
# class Brand:
#     __model="LG"
#     def get_model(self):
#         return self.__model
    
#     def set_model(self,model):
#         self.__model=model

# obj=Brand()
# print(obj.get_model())
# obj.set_model("Samsung")
# print(obj.get_model())