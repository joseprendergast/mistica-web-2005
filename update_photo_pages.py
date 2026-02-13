#!/usr/bin/env python3
import os
import re

base_path = "Mistica New Generation/Fotos"

# Gallery configurations: (directory, total_photos, image_pattern_function)
galleries = [
    ("Concierto 10_Junio_2005", 20, lambda n: f"{n}%20copia.jpg"),
    ("Concierto 2_Abril_2005", 7, lambda n: f"{n}.jpg"),
    ("Fotos_Grupo", 15, lambda n: {
        1: "Mist26.jpg", 2: "Mist2.jpg", 3: "Mist3.jpg", 4: "Mist4.jpg",
        5: "Mist1.jpg", 6: "Mist7.jpg", 7: "Mist9.jpg", 8: "Mist12.jpg",
        9: "Mist14.jpg", 10: "Mist16.jpg", 11: "Mist17.jpg", 12: "Mist18.jpg",
        13: "Mist23.jpg", 14: "Mist24.jpg", 15: "sky_lopez2(SPECIAL).jpg"
    }.get(n, f"Mist{n}.jpg"))
]

template = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>www.Mistica.tk</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<style type="text/css">
<!--
body {{
	background-color: #660000;
	margin: 0;
	padding: 0;
}}
.nav-container {{
	position: relative;
	display: inline-block;
	margin: 20px 0;
}}
.nav-arrow {{
	position: absolute;
	top: 50%;
	transform: translateY(-50%);
	background-color: rgba(0, 0, 0, 0.6);
	color: #FFFF99;
	border: 2px solid #FFFF99;
	font-size: 30px;
	padding: 15px 20px;
	cursor: pointer;
	text-decoration: none;
	user-select: none;
	transition: background-color 0.3s;
	z-index: 10;
}}
.nav-arrow:hover {{
	background-color: rgba(0, 0, 0, 0.8);
}}
.nav-arrow.left {{
	left: 20px;
}}
.nav-arrow.right {{
	right: 20px;
}}
.nav-arrow.disabled {{
	opacity: 0.3;
	cursor: not-allowed;
}}
.photo-info {{
	color: #FFFF99;
	font-family: Arial, Helvetica, sans-serif;
	margin: 10px 0;
	font-size: 14px;
}}
-->
</style>
<script src="../photo-navigation.js"></script>
</head>

<body>
<div align="center">
  <div class="nav-container">
    <a href="#" class="nav-arrow left" onclick="if(window.photoNav) window.photoNav.prev(); return false;" id="prevArrow">&lt;</a>
    <img src="{image_src}" width="{img_width}" height="{img_height}" id="photoImage">
    <a href="#" class="nav-arrow right" onclick="if(window.photoNav) window.photoNav.next(); return false;" id="nextArrow">&gt;</a>
  </div>
  <div class="photo-info">
    <span id="photoCounter">{current_num} / {total_photos}</span>
  </div>
  <p>&nbsp;</p>
  <p><img src="../../IndexImagenes/MiniMistica.gif" width="397" height="214"></p>
</div>
<script>
// Update navigation arrows and counter
(function() {{
    const currentFile = window.location.pathname.split('/').pop();
    const currentNum = parseInt(currentFile.replace('.htm', ''));
    const totalPhotos = {total_photos};
    
    // Update counter
    document.getElementById('photoCounter').textContent = currentNum + ' / ' + totalPhotos;
    
    // Update arrow states
    if (currentNum === 1) {{
        document.getElementById('prevArrow').classList.add('disabled');
        document.getElementById('prevArrow').onclick = function() {{ return false; }};
    }}
    if (currentNum === totalPhotos) {{
        document.getElementById('nextArrow').classList.add('disabled');
        document.getElementById('nextArrow').onclick = function() {{ return false; }};
    }}
}})();
</script>
</body>
</html>'''

def update_photo_page(gallery_dir, photo_num, total_photos, image_pattern_func, img_width=800, img_height=600):
    file_path = os.path.join(base_path, gallery_dir, f"{photo_num}.htm")
    
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} does not exist")
        return
    
    # Get image source
    image_src = image_pattern_func(photo_num)
    
    # Special handling for Fotos_Grupo - check actual image dimensions
    if gallery_dir == "Fotos_Grupo":
        img_width = 800
        img_height = 600
    
    # Generate HTML
    html_content = template.format(
        image_src=image_src,
        img_width=img_width,
        img_height=img_height,
        current_num=photo_num,
        total_photos=total_photos
    )
    
    # Write file
    with open(file_path, 'w', encoding='iso-8859-1') as f:
        f.write(html_content)
    
    print(f"Updated: {file_path}")

# Update all galleries
for gallery_dir, total_photos, image_pattern_func in galleries:
    print(f"\nUpdating gallery: {gallery_dir}")
    for photo_num in range(1, total_photos + 1):
        # Determine image dimensions based on gallery
        if gallery_dir == "Concierto 10_Junio_2005":
            img_width, img_height = 800, 600
        elif gallery_dir == "Concierto 2_Abril_2005":
            img_width, img_height = 567, 425
        else:  # Fotos_Grupo
            img_width, img_height = 800, 600
        
        update_photo_page(gallery_dir, photo_num, total_photos, image_pattern_func, img_width, img_height)

print("\nAll photo pages updated!")
