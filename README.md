# weather
Dit is een programma waarin je data kunt opvragen over steden over de hele wereld, en dat het de huidige weersomstandigheden laat zien

# Taal
Python 3.9

# Wat heb ik geleerd

  * Interactive maps in een tkinter app zetten
  * Meer tkinter details
  
# Gebruikte files

 * weerstation_app : main_file, staat alle data in wat te maken heeft met tkinter, waaronder tkintermapview
 * weerstation_datafile : data_file, alle data, waaronder details zoals schermgrootte etc
 * weerstation_locatie : class_file, wordt alle data word gesorteerd and opgeslagen
 * weerstation_api_response : functie_file, simpele functie die de API aanslaat en data teruggeeft
 * weerstation_export: function_file, functie waarin alle data in een worddocument gezet wordt
 


# Bedoeling van het programma
Wanneer je de app opent, moet er een entrybox komen, waarin je een stad/dorp kunt invoeren. Als je op 'start search' klikt, moet het programma huidig weerdata ophalen uit een API, en deze data weergeven. Ook moet er een map tevoorschijn komen, gefocust op de locatie die je hebt ingevoerd. Nadat dit allemaal is weergegeven,
moet er een .docx document komen waarin alle data wordt weergegeven. De titel van dit .docx moet gelijk zijn aan: '{locatie} {datum} {tijd}.docx'. Als je opnieuw een
andere stad of dorp invoert, moet alle data verwijdert worden, waaronder de map, en alle nieuwe data moet worden weergegeven.

# Problemen bij het programeren
Niets. Tkintermapview is behoorlijk straightforward, dus ik liep tegen geen problemen aan toen ik het probeerde te leren. Verder had ik alle andere libraries al een 
keer gebruikt, en daardoor ging het behoorlijk makkelijk. Het enige wat misschien als een probleem gezien kan worden, was dat, toen ik een ':' probeerde te gebruiken binnen een .docx filename, ik het niet voor elkaar kreeg om het als een .docx op te slaan.

## Bijlage
![Example_weatherstation](https://user-images.githubusercontent.com/107985687/226836442-4a414b31-6b85-4b22-a74e-ee6f2fe6f9cc.png)

^ Voorbeeld van de app
 
 ![Example_weatherstation_word](https://user-images.githubusercontent.com/107985687/226836540-327ea664-e427-4dc9-90e9-ee25a8874f8e.png)
 ^ Voorbeeld van de word_file

 
