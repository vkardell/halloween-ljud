# halloween-ljud

Skräckljud för Halloween-skrämman i Home Assistant, servade via jsDelivr så att Google Cast-högtalarna kan hämta dem snabbt:

```
https://cdn.jsdelivr.net/gh/vkardell/halloween-ljud@v2/<fil>.mp3
```

## Filerna

Elva MP3:or (192 kbit/s, 44,1 kHz) från archive.org-paketet
[Ringtonehorrorscreamssoundeffect270204](https://archive.org/details/Ringtonehorrorscreamssoundeffect270204).
Paketet anger ingen licens.

Originalen börjar med 2,75–4,0 s tystnad. Här är tystnaden bortklippt så att ljudet börjar efter cirka 0,1 s.
Klippningen sker på MP3-ramgränser utan omkodning, så resten av ljudet är bit för bit identiskt med originalet.

## Musiken

I `musik/` ligger fyra spår som loopas efter skrämman tills grinden laddar om, oförändrade från incompetech.com:

- "Myst on the Moor" Kevin MacLeod (incompetech.com)
- "Gathering Darkness" Kevin MacLeod (incompetech.com)
- "Ghost Story" Kevin MacLeod (incompetech.com)
- "Spellbound" Kevin MacLeod (incompetech.com)

Licensed under Creative Commons: By Attribution 4.0 License
http://creativecommons.org/licenses/by/4.0/

## Klippa en ny fil

```
python3 trim_mp3.py original.mp3 klippt.mp3 <sekunder att ta bort>
```

Skriptet hanterar bara CBR-MP3 i 44,1 kHz (som filerna i paketet) och har inga beroenden utöver Python 3.
Sätt sekunderna till tiden för första hörbara ljud minus 0,1.

Efter en ändring: committa, skapa en ny tagg (`v2` osv.) och peka om URL:erna i Home Assistant till den taggen.
jsDelivr cachar en tagg för alltid.
