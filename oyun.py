pencere.listen()
pencere.onkey(yukarı, "w")
pencere.onkey(aşağı, "s")
pencere.onkey(sağ, "d")
pencere.onkey(sol, "a")

oyun_devam_ediyor = True
while oyun_devam_ediyor:
  pencere.update()
  hareket()

  # Yılanın kendine çarpmasını kontrol edin
  for parça in kuyruklar:
    if parça.distance(yılan) < 20:
      oyun_devam_ediyor = False
      break

  # Yemeği yiyince kuyruğu uzatın ve yeni bir yemek oluşturun
  if yılan.distance(yemek) < 20:
    kuyruk_uzunluğu += 1
    yeni_kuyruk = turtle.Turtle()
    yeni_kuyruk.speed(0)
    yeni_kuyruk.shape("square")
    yeni_kuyruk.color(random.choice(["red", "green", "blue", "purple"]))
    yeni_kuyruk.penup()
    son_kuyruk = kuyruklar[-1]
    yeni_kuyruk.goto(son_kuyruk.xcor(), son_kuyruk.ycor())
    kuyruklar.append(yeni_kuyruk)
    yemek.goto(random.randint(-280, 280), random.randint(-280, 280))

  # Kuyruğu hareket ettirin
  for i in range(kuyruk_uz
