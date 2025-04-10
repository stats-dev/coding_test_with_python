a,b,c=map(int, input().split())

sum_abc = a+b+c
avg_abc = (a+b+c)//3 # 3의 배수이므로
sub_abc = sum_abc - avg_abc


print(f"{sum_abc}\n{avg_abc}\n{sub_abc}")
