# Brute force
# Time: O(n ** 2), space: O(n), n = longest length or s1, s2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        for i in range(len(s2) - len(s1) + 1):
                sorted_sub_s2 = sorted(s2[i:len(s1) + i])
                
                if sorted_sub_s2 == sorted_s1:
                    return True
        return False
                    
        

#list_s1 = ["a", "b", "c"]
#i = 0 => s2[i] = "d"  in list_s1 => list_s1.remove("d") = ["a", "c"]
#i = 1 => s2[i] = "c" in list_s1 => list_s1.remove("c") => ["a"]
#i = 2 => s2[i] = "d" not in list_s1 => list_s1 = ["a", "d", "c"]
#i = 3 => 



# Brute force
# Time: O(n ** m), space: O(m), n = length of s2, m = length of s1
#s1 = "abc", s2 = "lecabee"
#i = index of s2
#list_s1 = [for c in s1]
#copy_s1 = list_s1
#for i in range(len(n) - len(m)):
#i = 0:
#=> s2[i] = "l" not in copy_s1 => copy_s1 = list_s1
#
#i = 1: 
#=> s2[i] = "e" not in copy_s1 => copy_s1 = list_s1
#
#
#i = 2: 
#=> s2[i] = "c" in copy_s1 => copy_s1.remove(s2[i])
#
#i = 3:
#=> s2[i] = "a" in copy_s1 => copy_s1.remove(s2[i])
#
#i = 4:
#=> s2[i] = "b" in copy_s1 => copy_s1.remove(s2[i]) => copy_s1 == [] => return True
#
#











## Time: O(n + m), space: O(m), n = length of s2, m = length of s1 
#s1 = "abc", s2 = "lecabee"
#
#i = 0 
#s1_dict = {"a": 1, "b": 1, "c": 1}, count : 3
#j = 0 => s2[j] = "l" not in s1_dict => i += 1, continue
#
#i = 1
#s1_dict = {"a": 1, "b": 1, "c": 1}, count : 3
#j = 1  => s2[j] = "e" not in s1_dicgt => i += 1, continue
#
#i = 2
#s1_dict = {"a": 1, "b": 1, "c": 1}
#j = 2 => s2[j] = "c"  in s1_dict => si_dict[s2[j]] -= 1



