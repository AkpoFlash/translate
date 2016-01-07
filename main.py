import io

translation_map = {
					ord("а"):"a",
					ord("б"):"b",
					ord("в"):"v",
					ord("г"):"g",
					ord("д"):"d",
					ord("е"):"e",
					ord("ё"):"yo",
					ord("ж"):"zh",
					ord("з"):"z",
					ord("и"):"i",
					ord("й"):"j",
					ord("к"):"k",
					ord("л"):"l",
					ord("м"):"m",
					ord("н"):"n",
					ord("о"):"o",
					ord("п"):"p",
					ord("р"):"r",
					ord("с"):"s",
					ord("т"):"t",
					ord("у"):"u",
					ord("ф"):"f",
					ord("х"):"h",
					ord("ц"):"ts",
					ord("ч"):"ch",
					ord("ш"):"sh",
					ord("щ"):"sch",
					ord("ь"):"'",
					ord("ъ"):"\"",
					ord("ы"):"y",
					ord("э"):"e",
					ord("ю"):"yu",
					ord("я"):"ya",
					ord("А"):"A",
					ord("Б"):"B",
					ord("В"):"V",
					ord("Г"):"G",
					ord("Д"):"D",
					ord("Е"):"E",
					ord("Ё"):"Yo",
					ord("Ж"):"Zh",
					ord("З"):"Z",
					ord("И"):"I",
					ord("Й"):"J",
					ord("К"):"K",
					ord("Л"):"L",
					ord("М"):"M",
					ord("Н"):"N",
					ord("О"):"O",
					ord("П"):"P",
					ord("Р"):"R",
					ord("С"):"S",
					ord("Т"):"T",
					ord("У"):"U",
					ord("Ф"):"F",
					ord("Х"):"H",
					ord("Ц"):"Ts",
					ord("Ч"):"Ch",
					ord("Ш"):"Sh",
					ord("Щ"):"Sch",
					ord("Ы"):"Y",
					ord("Э"):"E",
					ord("Ю"):"Yu",
					ord("Я"):"Ya"
					}

input_file = open("input.txt","r", encoding="utf-8")
read_file = input_file.read()
input_file.close()

output_file = open("output.txt", "w", encoding="utf-8")
output_file.write(read_file.translate(translation_map))
output_file.close()

input("End of program")