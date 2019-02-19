from django.db import models
from django.urls import reverse


class UrlModel(models.Model):
    l_url = models.CharField(max_length=100)

    def get_sum(self, letters):
        sum = 0
        for l in letters:
            sum += ord(l)

        return sum

    @property
    def url_id(self):
        my_id = self.get_sum(self.l_url)

        #my_id = ord(self.l_url[0])
        return my_id

    @property
    def s_url(self):
        characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't',
                      'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                      'N',
                      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6',
                      '7', '8', '9']

        url = ''
        id = self.url_id
        while int(id) > 0:
            append = characters[int(id % 62)]
            url += append
            id /= 62

        return url[::-1]

    def get_absolute_url(self):
        return reverse('url_ready', kwargs={'pk': self.pk})

    def __str__(self):
        return self.l_url


