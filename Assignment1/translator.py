fp = open("32_bit.asm")
lines=fp.readlines()
string=""
for line in lines:
    #print line 
    if line=="int 0x80\n":
       line="syscall"+"\n"
    if line=="mov eax, 4\n":
       line="mov rax, 1\n"
    if line=="mov eax, 1\n":
       line="mov rax, 60\n"
    string=string+line

#print string
ans=string.split("\n")
final_string=""
for i in ans:
    small=i.split(" ")
    #print small
    for j in small:
        if j=="eax":
	   j="rax "
	if j=="eax,":
	   j="rax, "
	if j=="ebx":
	   j="rdi "
	if j=="ebx,":
	   j="rdi, "
	if j=="ecx":
	   j="rsi "
	if j=="ecx,":
	   j="rsi, "
	if j=="edx":
	   j="rdx "
	if j=="edx,":
	   j="rdx, "
	if j=="esp":
	   j="rsp "
	if j=="esp,":
	   j="rsp, "
	final_string=final_string+j+" "
    final_string=final_string+"\n"
#print final_string
f = open("64_bit.asm",'w')
f.write(final_string)
f.close()

