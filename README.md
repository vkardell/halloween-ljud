# halloween-ljud

Skräckljud för Halloween-skrämman i Home Assistant, servade via jsDelivr så att Google Cast-högtalarna kan hämta dem snabbt:

```
https://cdn.jsdelivr.net/gh/vkardell/halloween-ljud@v3/<fil>.mp3
```

## Filerna

Elva MP3:or (192 kbit/s, 44,1 kHz) från archive.org-paketet
[Ringtonehorrorscreamssoundeffect270204](https://archive.org/details/Ringtonehorrorscreamssoundeffect270204).
Paketet anger ingen licens.

Originalen börjar med 2,75–4,0 s tystnad. Här är tystnaden bortklippt så att ljudet börjar efter cirka 0,1 s.
Klippningen sker på MP3-ramgränser utan omkodning, så resten av ljudet är bit för bit identiskt med originalet.

## Musiken

I `musik/` ligger spåren som loopas efter skrämman tills grinden laddar om.

Fyra spår är oförändrade från incompetech.com:

- "Myst on the Moor" Kevin MacLeod (incompetech.com)
- "Gathering Darkness" Kevin MacLeod (incompetech.com)
- "Ghost Story" Kevin MacLeod (incompetech.com)
- "Spellbound" Kevin MacLeod (incompetech.com)

Licensed under Creative Commons: By Attribution 4.0 License
http://creativecommons.org/licenses/by/4.0/

Fem speldosespår kommer från OpenGameArt. De är omkodade till MP3 med `make_loop_mp3.py`, och de som loopar sömlöst är upprepade några gånger i filen så att det blir färre pauser när Home Assistant startar om spåret:

- `forgotten_lullaby.mp3`: "Forgotten Lullaby" (Music Box Loop, 8 gånger). Music by Mega Pixel Music Lab, megapixelmusiclab.com. CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. Källa: https://opengameart.org/content/forgotten-lullaby
- `broken_carousel_waltz.mp3`: Music: "Broken Carousel Waltz" by Arold Valda. Licensed under CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. Källa: https://opengameart.org/content/broken-carousel-waltz
- `sad_tune.mp3` (2 gånger) och `spooky_waltz.mp3` (2 gånger): "musicbox3_sad_tune" och "musicbox1_spooky_waltz" av Aureolus_Omicron. CC0. Källa: https://opengameart.org/content/4-music-box-tracks
- `creepy_lullaby.mp3`: "Creepy lullaby (short)" av iletzy (11 gånger). CC BY-SA 3.0, https://creativecommons.org/licenses/by-sa/3.0/. Den upprepade filen delas under samma licens. Källa: https://opengameart.org/content/creepy-lullaby-short

## Göra en loopfil

```
python3 -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/python make_loop_mp3.py original.ogg musik/namn.mp3 <antal upprepningar>
```

## Klippa en ny fil

```
python3 trim_mp3.py original.mp3 klippt.mp3 <sekunder att ta bort>
```

Skriptet hanterar bara CBR-MP3 i 44,1 kHz (som filerna i paketet) och har inga beroenden utöver Python 3.
Sätt sekunderna till tiden för första hörbara ljud minus 0,1.

Efter en ändring: committa, skapa en ny tagg (`v4` osv.) och peka om URL:erna i Home Assistant till den taggen.
jsDelivr cachar en tagg för alltid.
