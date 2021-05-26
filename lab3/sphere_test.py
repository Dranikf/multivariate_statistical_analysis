from easy_sphere_plotter import just_plot_sphere
import matplotlib.pyplot as plt

# создаем окошко для отрисовки
fig = plt.figure(figsize = [20, 15])
# в нем создаем оси с поддежкой 3д
ax = fig.add_subplot(111, projection='3d')

# чудо функция
# первым аргументом центр сферы
# вторым радиус
# третьим созданные выше оси
# именованые аргументы спецификация как тут https://matplotlib.org/2.0.2/mpl_toolkits/mplot3d/tutorial.html для функции plot_surface
my_plot = just_plot_sphere([1,1,1], 5, ax, color = "red")
# на выходе получаем объект описывающий эту сферу
# можно поменять его свойства всякие, например прозрачность
my_plot.set_alpha(0.5)
# настройки этой штуки можно посмотреть тут https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html

plt.show()