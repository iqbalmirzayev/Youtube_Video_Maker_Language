from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
from moviepy.editor import *
import glob
from constants import font_roman,image_path,language
import subprocess
import os

class Processor:
    @classmethod
    def word_to_image(cls, word,id):
        image = Image.open(image_path)
        width, height = image.size
        center_x = width // 2
        center_y = height // 2
        word_layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(word_layer)
        font_size = 100
        font = ImageFont.truetype(font_roman, font_size)
        word_width, word_height = draw.textsize(word, font=font)
        word_x = center_x - word_width // 2
        word_y = center_y - word_height // 2
        draw.text((word_x, word_y), word, font=font, fill=(255, 255, 255, 255), align="center")
        
        # Save the image to a file
        image_with_word = Image.alpha_composite(image.convert('RGBA'), word_layer)
        image_with_word.save('folders/{}/word_{}.png'.format(id,id))  
        # Save the audio 
        speech= gTTS(text=word,lang=language,slow=False,tld="com.au")
        speech.save("folders/{}/word_{}.mp3".format(id,id))
        # Save the video 
        # audio = AudioFileClip("folders/{}/word_{}.mp3".format(id,id))
        # photo=('folders/{}/word_{}.png'.format(id,id))
        # clip = ImageClip(photo).set_duration(audio.duration)
        # clip = clip.set_audio(audio)
        # clip.write_videofile(f"folders/{id}/word_{id}.mp4", fps=24)
        ffmpeg_cmd = f'ffmpeg -loop 1 -i folders/{id}/word_{id}.png -i folders/{id}/word_{id}.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest folders/{id}/word_video.mp4'
        subprocess.call(ffmpeg_cmd, shell=True)
        # os.remove(f"folders/{id}/word_{id}.png")
        # os.remove(f"folders/{id}/word_{id}.mp3")
        with open (f"folders/{id}/i.txt","w") as f:
            f.write("word_video.mp4\n")

        
    @classmethod
    def word_part_to_image(cls, word_part,id):
        image = Image.open(image_path)
        width, height = image.size
        center_x = width // 2
        center_y = height // 2
        text_layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(text_layer)
        font_size = 100
        font = ImageFont.truetype(font_roman, font_size)
        text_width, text_height = draw.textsize(word_part, font=font)
        text_x = center_x - text_width // 2
        text_y = center_y - text_height // 2
        draw.text((text_x, text_y), word_part, font=font, fill=(255, 255, 255, 128), align="center")
        image_with_text = Image.alpha_composite(image.convert('RGBA'), text_layer)
        # Save the image to a file
        image_with_text.save('folders/{}/word_part_{}.png'.format(id,id))  
        # Save the audio
        speech= gTTS(text=word_part,lang=language,slow=False,tld="com.au")
        speech.save("folders/{}/word_part_{}.mp3".format(id,id))
        # Save the video
        # audio = AudioFileClip("folders/{}/word_part_{}.mp3".format(id,id))
        # photo=('folders/{}/word_part_{}.png'.format(id,id))
        # clip = ImageClip(photo).set_duration(audio.duration)
        # clip = clip.set_audio(audio)
        # clip.write_videofile(f"folders/{id}/word_part_{id}.mp4", fps=24)
        
        ffmpeg_cmd = 'ffmpeg -loop 1 -i folders/{}/word_part_{}.png -i folders/{}/word_part_{}.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest folders/{}/word_part_video.mp4'.format(id,id,id,id,id)
        with open (f"folders/{id}/i.txt","a") as f:
            f.write("word_part_video.mp4\n")
        # ffmpeg_cmd2=f'ffmpeg -i folders/{id}/word_video.mp4 -i folders/{id}/word_part_video.mp4 -filter_complex "[0:v:0][1:v:0]concat=n=2:v=1:a=0" -c:v libx264 -crf 18 -preset veryslow -y folders/{id}/video_{id}.mp4'
        # ffmpeg_cmd2=f'ffmpeg -i folders/{id}/word_video.mp4 -i folders/{id}/word_part_video.mp4 -filter_complex "[0:v:0][1:v:0]concat=n=2:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -crf 18 -preset veryslow -c:a aac -b:a 192k -pix_fmt yuv420p -y folders/{id}/video_{id}.mp4'
        # ffmpeg_cmd2='ffmpeg -f concat -safe 0 -i folders/{}/input.txt -c copy folders/{}/video_{}.mp4'.format(id,id,id)
        subprocess.call(ffmpeg_cmd, shell=True)
        # subprocess.call(ffmpeg_cmd2, shell=True)
        # os.remove(f"folders/{id}/word_part_{id}.png")
        # os.remove(f"folders/{id}/word_part_{id}.mp3")
        # os.remove(f"folders/{id}/word_part_video.mp4")
        # os.remove(f"folders/{id}/word_video.mp4")
        # os.remove(f"folders/{id}/input.txt")

    @classmethod
    def meaning_image(cls, word,id):
        image = Image.open(image_path)
        width, height = image.size
        center_x = width // 2
        center_y = height // 2
        word_layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(word_layer)
        font_size = 100
        font = ImageFont.truetype(font_roman, font_size)
        word_width, word_height = draw.textsize(word, font=font)
        word_x = center_x - word_width // 2
        word_y = center_y - word_height // 2
        draw.text((word_x, word_y), word, font=font, fill=(255, 255, 255, 128), align="center")
        
        # Save the image to a file
        image_with_word = Image.alpha_composite(image.convert('RGBA'), word_layer)
        image_with_word.save('folders/{}/meaning.png'.format(id))  
        # Save the audio 
        speech= gTTS(text=word,lang=language,slow=False,tld="com.au")
        speech.save("folders/{}/meaning.mp3".format(id))
        # Save the video 
        # audio = AudioFileClip("folders/{}/word_{}.mp3".format(id,id))
        # photo=('folders/{}/word_{}.png'.format(id,id))
        # clip = ImageClip(photo).set_duration(audio.duration)
        # clip = clip.set_audio(audio)
        # clip.write_videofile(f"folders/{id}/word_{id}.mp4", fps=24)
        ffmpeg_cmd = f'ffmpeg -loop 1 -i folders/{id}/meaning.png -i folders/{id}/meaning.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest folders/{id}/meaning.mp4'
        subprocess.call(ffmpeg_cmd, shell=True)
        # os.remove(f"folders/{id}/meaning.png")
        # os.remove(f"folders/{id}/meaning.mp3")
        with open (f"folders/{id}/i.txt","a") as f:
            f.write("meaning.mp4\n")
    a=[]
    @classmethod
    def meaning_to_image(cls, id,meaning):
        
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        font_size = 30
        font = ImageFont.truetype(font_roman, font_size)
        print("FONT", dir(font))
        width, height = image.size
        lines = []
        if font.getsize(meaning)[0] <= width:
            lines.append(meaning)
        else:
            words = meaning.split(' ')
            i = 0
            while i < len(words):
                line = ''
                while i < len(words) and font.getsize(line + words[i])[0] <= width:
                    line = line + words[i] + " "
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                lines.append(line)
        y_meaning = height / 2
        for i, line in enumerate(lines):
            line_width, line_height = font.getsize(line)
            x = (width - line_width) / 2
            y = y_meaning- line_height * len(lines) / 2 + i * line_height
            draw.text((x, y), line, font=font, fill=(255, 255, 255, 128))
        cls.a.append(meaning)
        # Save image
        image.save("folders/{}/meaning_{}.png".format(id,len(cls.a)))
        # Save audio
        speech= gTTS(text=meaning,lang=language,slow=False,tld="com.au")
        speech.save("folders/{}/meaning_{}.mp3".format(id,len(cls.a)))
        # Save Video
        # audio = AudioFileClip("folders/{}/meaning_{}.mp3".format(id,len(a)))
        # photo=('folders/{}/meaning_{}.png'.format(id,len(a)))
        # clip = ImageClip(photo).set_duration(audio.duration)
        # clip = clip.set_audio(audio)
        # clip.write_videofile(f"folders/{id}/video_meaning{len(a)}.mp4", fps=24)
        ffmpeg_cmd = f'ffmpeg -loop 1 -i folders/{id}/meaning_{len(cls.a)}.png -i folders/{id}/meaning_{len(cls.a)}.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -speed 10  -shortest folders/{id}/meaning_video_{len(cls.a)}.mp4'
        subprocess.call(ffmpeg_cmd, shell=True)
        with open (f"folders/{id}/i.txt","a") as f:
            f.write(f"meaning_video_{len(cls.a)}.mp4\n")
        # os.remove(f"folders/{id}/meaning_{len(cls.a)}.png")
        # os.remove(f"folders/{id}/meaning_{len(cls.a)}.mp3")
            
    b=[]  
    @classmethod
    def phrase_to_image(cls, id,phrase):
        
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        font_size = 150 
        font = ImageFont.truetype(font_roman, font_size)
        print("FONT", dir(font))
        width, height = image.size
        lines = []
        if font.getsize(phrase)[0] <= width:
            lines.append(phrase)
        else:
            words = phrase.split(' ')
            i = 0
            while i < len(words):
                line = ''
                while i < len(words) and font.getsize(line + words[i])[0] <= width:
                    line = line + words[i] + " "
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                lines.append(line)
        y_meaning = height / 2
        for i, line in enumerate(lines):
            line_width, line_height = font.getsize(line)
            x = (width - line_width) / 2
            y = y_meaning- line_height * len(lines) / 2 + i * line_height
            draw.text((x, y), line, font=font, fill=(255, 255, 255, 128))
        cls.b.append(phrase)
        # Save image
        image.save("folders/{}/phrase_{}.png".format(id,len(cls.b)))
        # Save audio
        speech= gTTS(text=phrase,lang=language,slow=False,tld="com.au")
        speech.save("folders/{}/phrase_{}.mp3".format(id,len(cls.b)))
        # Save Video
        # audio = AudioFileClip("folders/{}/phrase_{}.mp3".format(id,len(a)))os.        
        # photo=('folders/{}/phrase_{}.png'.format(id,len(a)))
        # clip = ImageClip(photo).set_duration(audio.duration)
        # clip = clip.set_audio(audio)
        # clip.write_videofile(f"folders/{id}/video_phrase{len(a)}.mp4", fps=24)
        ffmpeg_cmd = f'ffmpeg -loop 1 -i folders/{id}/phrase_{len(cls.b)}.png -i folders/{id}/phrase_{len(cls.b)}.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest folders/{id}/phrase_video{len(cls.b)}.mp4'
        subprocess.call(ffmpeg_cmd, shell=True)
        with open (f"folders/{id}/i.txt","a") as f:
            f.write(f"phrase_video_{len(cls.b)}.mp4\n")
        # os.remove(f"folders/{id}/phrase_{len(cls.b)}.png")
        # os.remove(f"folders/{id}/phrase_{len(cls.b)}.mp3")
        
    @classmethod
    def concatenate_all_videos(cls, id):
        folder_url = f"folders/{id}/"
        all_lines = []
        with open(f"{folder_url}i.txt") as f:
            for line in f:
                line = line[:-1]
                print(repr(line))
                abs_path = os.path.abspath(f"{folder_url}{line}")
                full_line = f"file '{abs_path}'\n"
                print(full_line)
                all_lines.append(full_line)
        with open(f"{folder_url}input.txt","w") as f1:
            f1.writelines(all_lines)
        ffmpeg_cmd2='ffmpeg -f concat -safe 0 -i folders/{}/input.txt -c copy -speed 10 folders/{}/video_{}.mp4'.format(id,id,id)
        subprocess.call(ffmpeg_cmd2, shell=True)
        for i in all_lines:
            i=i[6:-2]
            # print(type(i))
        #     os.remove(i)
        # os.remove(f"folders/{id}/input.txt")
        