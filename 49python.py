#49 EL CALENDARIO DE ADEVIENTO 2022
"""
 * ¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software, ciencia y tecnología desde el 1 de diciembre.
 *
 * Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne lo siguiente:
 * - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
 * - Si la fecha es anterior: Cuánto queda para que comience el calendario.
 * - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
 *
 * Notas:
 * - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00 y finaliza a las 23:59:59.
 * - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos y segundos.
"""

#list of prizes
prizes = ['House', 'Car', 'Doll', 'Lego Set', 'Book I', 'Book II', 'Book III', 'Book IV', 'Book V', 'PC Game', 'Ring', 'CD I',
           'CD II', 'CD III', 'CD IV', 'CD V', 'CD VI', 'New Magazine', 'Monitor', 'Keyboard', 'Mouse', 'Motorcycle', 'Hoodie','iPhone']

def dateInNumbers(date:str)-> str:
    """function to convert dates"""
    hours = int(date[0:2])
    minutes = int(date[3:5])
    seconds = int(date[6:8])
    day = int(date[9:11])
    month = int(date[12:14])
    year = int(date[15:19])

    #print(hours, minutes, seconds, day, month, year)
    # hours, minutes and seconds until midnight "23:59:59"
    # hours, minutes and seconds from midnight "23:59:59"

    #error control:
    if hours > 23 or minutes > 59 or seconds > 59 or day > 31 or month > 12:
        raise Exception("Wrong date.")
    
    if month < 12 and year <= 2022: #control before:
        beforeHours = 23 - hours 
        beforeMinutes = 59 - minutes
        beforeSeconds = 59 - seconds
        beforeDay = 31 - day
        beforeMonth = 12 - month - 1
        beforeYear = 2022 - year
    
        return print(f"You need to wait: {beforeHours} hours, {beforeMinutes} minutes, {beforeSeconds} seconds, {beforeDay} days, {beforeMonth} months and {beforeYear} years.")
    elif year > 2022: #control after next year:
        yearAfter = year - 2022 -1
        dayAfter = day + 31 - 24      
        return print(f"Calendar finished: {hours} hours, {minutes} minutes, {seconds} seconds, {dayAfter} days, {month - 1} months and {yearAfter} years ago.")
    elif month == 12 and year == 2022 and day > 24: #control after 24/12/2022:
        afterDay = day - 25
        return print(f"Calendar finished: {hours} hours, {minutes} minutes, {seconds} seconds, {afterDay} days, 0 months and 0 years ago.")
    else: #day of the draw
        beforeHours = 23 - hours 
        beforeMinutes = 59 - minutes
        beforeSeconds = 59 - seconds
        return print(f"Your prize is: {prizes[day-1]}. Today's draw finish in: {beforeHours} hours, {beforeMinutes} minutes and {beforeSeconds} seconds.")


dateInNumbers("04:05:22 11/11/2022")
dateInNumbers("04:05:22 11/11/2020")
dateInNumbers("11:19:55 29/12/2022")
dateInNumbers("11:19:55 01/02/2023")
dateInNumbers("14:19:45 12/12/2022")
dateInNumbers("21:33:25 24/12/2022")


