import os, csv

with open("100MostStreamedSongs.csv") as file:
  f = csv.reader(file)

  for row in f:
    tempArtist = row[3]
    # create dir if it doesn't exist
    try:
      os.mkdir(tempArtist)
    except:
      pass
    # create file in sub-dir
    tempSong = open(f"{tempArtist}/{row[1]}.txt","w")
    tempSong.close()

exit()
