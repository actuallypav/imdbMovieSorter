import imdb
ia = imdb.IMDb()
f = open("mov.txt", "r")
newF = open("list.txt", "w")
i = 0
newFList = []
with open("mov.txt", "r") as f:
    for line in f:
        movies = ia.search_movie(line)
        print(movies)
        id = movies[0].movieID
        getMovie = ia.get_movie(id)
        year = str(getMovie['year'])
        name = str(getMovie['title'])
        text = '<li> <a href="https://www.imdb.com/title/tt' + \
            str(id) + '/?ref_=vp_vi_tt">' + name + '</a>' + year + '</lis>'
        newFList.append(text)

with open("list.txt", "w") as newF:
    for line in newFList:
        newF.write(line + '\n')
