from exif import Image

fileLoc = input('Input file: ')
# with open('/mnt/c/temp/WP_20170323_15_23_12_Pro.jpg', 'rb') as image_file:
with open(fileLoc, 'rb') as image_file:
     my_image = Image(image_file)

# print(my_image.has_exif)
# print(dir(my_image))

# dto = '2021:03:23 15:23:12'
# dtd = '2021:03:23 15:23:15'
dto = input('Date-time-original (as 2021:03:23 15:23:12): ')
dtd = input('Date-time-digitized (as 2021:03:23 15:23:12): ')

my_image.datetime_original = dto
my_image.datetime_digitized = dtd

with open('/mnt/c/temp/wmodified_image.jpg', 'wb') as new_image_file:
     new_image_file.write(my_image.get_file())