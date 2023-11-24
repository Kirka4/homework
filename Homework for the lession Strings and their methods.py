str="Кот пошел гулять. Другой КОТ не пошел с ним, а кОты были не здесь, но кот был доволен, так же как и КОты"
word_count1 = str.count("кот")
word_count2 = str.count("КОТ")
word_count3 = str.count("Кот")
print("Количество слов кот в строке:", word_count1+word_count2+word_count3)