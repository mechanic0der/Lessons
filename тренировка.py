from random import randint


r = {"керамика":randint(20,100),"стекло":randint(20,100)}
t = 0
while r["керамика"] > 0 and r["стекло"] > 0:
    r["керамика"] -= 1
    r["стекло"] -= 1
    t += 1
print(f"Сделано {t} тарелок\nОсталось: {r} ресурсов")

