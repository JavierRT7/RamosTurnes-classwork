def reverse(word):
    if len(word) == 1:
        return letter
    else:
        return rev_word(word[1:]) + letter
    #End If
#End Function
print(reverse('STAR'))