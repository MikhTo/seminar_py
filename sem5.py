#для аппроксимации
import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    # В прошлый раз говорили о numpy -- билиотеке, 
    # которая позволяет быстро работать массивами, матрицами и прочими структурами,
    # с которыми сталкиваются физики в ежедневной работе

    # После того, как мы получили результат нашего моделирования/обработки эксп. данных и т.п.
    # Необходимо представить их в читаемом для людей виде.
    # Это можно сделать с помощью графиков, гистограмм, диограмм и т.п.
    # В Python это можно сделать через библиотеку matplotlib 
    
    # Семинар построим так: 
    # 1. Cначала познакомимся с библиотекой, отрисовав графики синтеического сигнала
    # 2. Обработаем реальный экспериментальный сигнал и воспользуемcя более продвинутыми фичами matplolib
    
    # Сначала создадим синтетический сигнал
    # Обычно сигналы представляются двумя массивами: 
    #   1. Первый массив хранит отсчеты времени
    #   2. Второй массив хранит значения физической величины, 
    #      которые соответсвуют отсетам первого массива

    # Делаем массив времен
    t = np.arange(-5, 5, 0.0001)
    # Делаем массив значений (3 синуса с разными амлитудой и частотой + случайный шум)
    sig = sum(a*np.sin(2*np.pi*f*t) 
              for a, f in zip([6, -3, 2], [150, 300, 450])) + np.random.uniform(-2,2,t.size)

    plt.figure()
    plt.plot(t, sig)
    plt.ylabel("Какая-то величина")
    plt.xlabel("Время")
    #plt.show()

    # Давайте теперь отфильтруем наш сигнал: снизим уровень шумов
    # Можно использовать для этого библиотку scipy (SCIentific PYthon)
    # В ней есть модул signal, откуда нам понадобятся функции:
    #   1. butter -- реализует фильтр Баттерворта (в signal есть и другие фильтры)
    #   2. sosfilt -- применяет фильтр к сигналу. Возвращает уже отфильтрованный сигнал.
    from scipy.signal import butter, sosfilt
    
    # Аргумент 1: Порядок фильтр (50)
    # Аргумент 2: Критическая частота(-ы)
    # Аргумент 3: Режим работы фильтра. 'bp' -- band pass 

    fs = 1 / (t[1]-t[0]) # Частота дискретизации

    sos = butter(50, [100, 500], 'bp', fs=fs,  output="sos")
    filtered = sosfilt(sos, sig)

    plt.figure()
    plt.plot(t, sig)
    plt.plot(t, filtered)
    #plt.show()

    #Также есть функция для построения гистограмм
    plt.figure()
    vals, bins, patches = plt.hist(sig - filtered)
    #plt.show()
    
    #Теперь давайте поработаем с реальным сигналом
    #Он у нас лежит в csv-файле
    res = np.genfromtxt('foo.csv', delimiter=';')
    t, sig = res[:,0], res[:,1]

    # Допустим хотим посмотреть форму сигнала, его Фурье, 
    # спектрограмму и зависимость частоты от эксперементальных параметров
    # И хотим объединить все три графика на одной фигуре
    # Для этого будем использовать subplots

    fig, axes = plt.subplots(2,2) #хотим четые графика в две строки и в два столбца 

    #Дальнейшее можно делать в цикле, но для наглядности обойдемся без него
    axes[0][0].plot(t, sig)
    
    #Украшаем график
    axes[0][0].set_xlabel("Время, мкс")
    axes[0][0].set_ylabel("$U_{emis}, В$")
    axes[0][0].set_title("Исходный сигнал")
    
    #plt.show()
    # Теперь посмотрим на Фурье
    # Для начала его надо вычислить
    # Можно воспользоваться модулем fft из numpy (схожие функции есть и в scipy)

    #Вычисляем частоты:
    freq = np.fft.rfftfreq(len(t), (t[1]-t[0])*10**-6)
    four = abs(np.fft.rfft(sig))
    axes[1][0].plot(freq[freq>100], four[freq>100])
    #Украшаем график
    axes[1][0].set_xlabel("Частота, Гц", fontsize=60)
    axes[1][0].set_ylabel(r"$\hat{F}$, у.е.", fontsize=60)
    axes[1][0].set_title("Фурье-образ")
    #Обычно Фурье изображают в логарифмических шкалах
    axes[1][0].set_xscale("log")
    axes[1][0].set_yscale("log")

    #plt.show()
    #Вычислить спектрограмму можено с помощью функции spectrogram из numpy
    from scipy.signal import spectrogram
    fs = 1/(t[1]-t[0])
    freq_sc, t_sc, spectrum = spectrogram(sig, fs=fs, window="hamming",  
                                          nperseg=int(10000*fs), noverlap=int(9900*fs))
    
    axes[0][1].pcolormesh(t_sc, freq_sc*10**3, spectrum, shading='nearest', 
                          cmap = plt.get_cmap('plasma'), vmax=250)
    axes[0][1].set_xlabel("t, мкс")
    axes[0][1].set_ylabel("f, кГц")
    axes[0][1].set_title("Спектрограмма")
    #plt.show()
    # Теперь нужно построить зависимость частоты от эксперментальных параметров
    # В качестве такого параметра выберем Альфеновскую скорость V_A = B/sqrt(4*pi*po)

    # наши данные лежат в эксельке
    # экспортируем их с помощью библиотеки pandas
    # (не будем на ней останавливаться, оставим для самостоятельного изучения)

    import pandas as pd
    B = [100, 70, 60, 50]

    exp_data = {f"{b} мТл": pd.read_excel("alphen_article_plot.xlsx", f"B{b}R75_f1").to_dict('list')
                for b in B}
    exp_data["all_merged"] = pd.read_excel("alphen_article_plot.xlsx", f"all_merged").to_dict('list')
    
    # Получили json'чик
    # Теперь можно работать

    styles = {100: {"marker":"*", "color":"purple"}, 70: {"marker":"s", "color":"red"},
              60: {"marker":"o", "color":"green"}, 50: {"marker":"^", "color":"blue"}}
    for b in B:
        axes[1][1].plot(exp_data[f"{b} мТл"]["V_A[m/s]"], exp_data[f"{b} мТл"]["freq_means 1"],  
                        linestyle="None", **styles[b], label = f"{b} мТл")
    
    # Добавим подписи (легенду)
    axes[1][1].legend(loc="lower right")
    # Добавим сетку
    axes[1][1].grid(which='major')
    axes[1][1].minorticks_on()
    axes[1][1].grid(which='minor', linestyle=':')

    #plt.show()

    # Можем захотеть сделать аппроксимацию в четвертом графике
    # Для этого можно воспользоваться функцией curve_fit из модуля scipy.optimize
    from scipy.optimize import curve_fit
    # Обязательные параметры: аппроксимирующая функция, значения по x и по y
    # Возвращает оптимальные параметры аппрокс.функции и матрицу ковариаций (для погрешностей)
    xdata = np.array(exp_data["all_merged"]["V_A[m/s]"])[np.array(exp_data["all_merged"]["V_A[m/s]"])<2.8*10**6]
    ydata = np.array(exp_data["all_merged"]["freq_means 1"])[np.array(exp_data["all_merged"]["V_A[m/s]"])<2.8*10**6] 
    
    f = lambda x, a, b: a*x+b
    popt, pcov = curve_fit(f=f,ydata=ydata, xdata=xdata)
    
    axes[1][1].plot(xdata, f(xdata, *popt))
    


    



    plt.show()
    pass