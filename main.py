import imdb
ia = imdb.IMDb()
f = open("mov.txt", "r")
newF = open("list.txt", "w")
newFList = []

# read the mov.txt with all the movie names
with open("mov.txt", "r") as f:
    for line in f:
        movies = ia.search_movie(line)

        try:
            # see the first value (will throw an error if it didn't find anything)
            id = movies[0].movieID
            getMovie = ia.get_movie(id)
            year = str(getMovie['year'])
            name = str(getMovie['title'])
            # format to HTML list item
            text = '<li> <a href="https://www.imdb.com/title/tt' + \
                str(id) + '/?ref_=vp_vi_tt">' + name + \
                '</a>' + " " + year + '</lis>'
        except:
            # search value returned nothing
            text = "ERROR - Movie " + line + " does not exist - ERROR"

        # append the list item to a newFList
        newFList.append(text)


# write newFList to list.txt
with open("list.txt", "w") as newF:
    for line in newFList:
        newF.write(line + '\n')
