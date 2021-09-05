# def calculate(num):
#     """
#     :param num: boundary
#     :return: result
#     """
#     res = 1
#     for i in range(2, num + 1, 2):
#         res *= i
#     return res
#
#
# print(calculate(10))
#
#
# def factorial(num):
#
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num - 1)
#
#
# print(factorial(5))

"""
This project is built in order to accomplish a simple voting system

Specificity: Voter can select vote one people or two people or no one. One vote got one point
"""


# class Vote:
#
#     def voting(self, candidate_dic, voter_list):
#
#         """This file is to build the voting system."""
#
#         voting_user_time = 1  # In order to make sure that the voting stops after every voters has voted
#         voters = voter_list
#         initial_user_len = len(voters)
#         while voting_user_time < initial_user_len + 1:
#             voter_name = (
#                 input('Please first write your voting name: '))
#             print('Hi ' + str(voter_name) + '! Welcome to our voting system')
#             if voter_name in voters:
#                 voters.remove(voter_name)
#                 vote_user_name = voter_name
#                 two_opportunity_flag = 1
#                 while two_opportunity_flag < 3:
#                     voter_choice = int(
#                         input(
#                             'Hello! ' +
#                             str(vote_user_name) +
#                             ' This if your ' +
#                             str(two_opportunity_flag) +
#                             ' selection. Please select the candidate '
#                             'you are going to vote: 1 -> A, 2 -> B, 3 -> C, 4 -> no one'))
#                     if voter_choice == 1:
#                         candidate_dic['Candidate1'] += 1
#                     elif voter_choice == 2:
#                         candidate_dic['Candidate2'] += 1
#                     elif voter_choice == 3:
#                         candidate_dic['Candidate3'] += 1
#                     elif voter_choice == 4:
#                         print('You did not select anyone')
#                     two_opportunity_flag += 1
#                 voting_user_time += 1
#             else:
#                 print('The voter has already voted, please select other voters.')
#                 continue
#         return candidate_dic
#
#     def calculate(self, candidate_dic, voter_list):
#
#         """This file is to count the points for different candidates"""
#
#         candidate_dic = self.voting(candidate_dic, voter_list)
#         candidate_dic.keys()
#         list_res = []
#         for val in candidate_dic.values():
#             list_res.append(val)
#         res = max(list_res)
#         playoff_dic = {}
#         if list_res.count(res) > 1:
#             print('The winner more than one')
#             for key in candidate_dic.keys():
#                 if candidate_dic[key] == res:
#                     print('winner: {}, point: {}'.format(key, res))
#                     new_pair = {key: res}
#                     playoff_dic.update(new_pair)
#             print(playoff_dic)
#             return playoff_dic
#
#         else:
#             new_dic = {}
#             for key in candidate_dic.keys():
#                 if candidate_dic[key] == res:
#                     print('winner: {}, point: {}'.format(key, res))
#                     new_dic[key] = res
#             return new_dic
#
#     def playoff(self, candidate_dic, voter_list):
#         playoff_team = self.calculate(candidate_dic, voter_list)
#         decision = len(list(playoff_team.values()))
#         if decision == 1:
#             print('voting is over')
#         else:
#             self.calculate(playoff_team, voter_list)
#
#
# v = Vote()
# """initial setting for candidates and voters"""
# a, b, c = 0, 0, 0
# candidates_dic = {
#     'Candidate1': a,
#     'Candidate2': b,
#     'Candidate3': c
# }
# voters_list = ['Tom', 'Luffy', 'Jerry']
# v.playoff(candidates_dic, voters_list)

