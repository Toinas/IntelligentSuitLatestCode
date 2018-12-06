
import numpy np

image=[0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,
0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,
0,  0,  0,  1,  1,  2,  2,  2,  2,  2,  2,  2,  1,  1,  0,  0,
0,  0,  1,  1,  2,  2,  2,  2,  2,  2,  2,  1,  1,  0,  0,  0,
0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  0,  0,
0,  0,  1,  1,  2,  1,  1,  2,  1,  1,  2,  1,  1,  0,  0,  0,
0,  0,  0,  1,  1,  2,  1,  1,  2,  1,  1,  2,  1,  1,  0,  0,
0,  0,  1,  1,  2,  2,  2,  2,  2,  2,  2,  1,  1,  0,  0,  0,
0,  0,  0,  0,  1,  1,  2,  2,  2,  2,  2,  1,  1,  0,  0,  0,
0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  0,  0,  0,  0,  0,
1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,
1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,
0,  0,  0,  0,  0,  0,  1,  1,  0,  1,  1,  0,  0,  0,  0,  0,
0,  0,  0,  0,  0,  1,  1,  0,  1,  1,  0,  0,  0,  0,  0,  0,
0,  0,  0,  0,  0,  0,  1,  1,  0,  1,  1,  0,  0,  0,  0,  0,
0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0]



def blit(image, img_width, location, frame_size):
    frame=['.'] * frame_size ** 2
    vert_offset=0

    img_lines = [image[x:x+img_width] for x in range(0,len(image),img_width)]
    for line in img_lines:
        for idx, value in enumerate(line):
            frame[idx+vert_offset+(location[0]*frame_size)+location[1]] = value
        vert_offset += frame_size

    return frame

def display(width, frame):
   lines = [frame[x:x+width] for x in range(0,len(frame),width)]
   for line in lines:
        print ' '.join(line)
 
def scrollimage(image):
    image = np.reshape(image, (16,16))
    np.roll(image,1, axis=1)
    return np.reshape(image,256)

if __name__ == "__main__":

        frame = blit(image, 16, [0,0], 16)
        display(16, frame)
		
        print "\n"
        new image = scrollimage(image)
        display(16, frame)

        # frame = blit(image, 3, [3,3], 16)
        # display(12, frame)

        # print "\n"

        # frame = blit(image, 3, [6,6], 16)
        # display(12, frame)

        # print "\n"

        # frame = blit(image, 3, [9,9], 16)
        # display(12, frame)
