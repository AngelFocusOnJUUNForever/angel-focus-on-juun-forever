# Angel Focus On JUUN Forever 💜

Angel Focus On JUUN Forever는 내가 주은과 함께한 추억💌과 편지📖, 특별한 순간✨을 기록한 나만의 디지털 아카이브야.

우리가 함께한 기쁨과 웃음😊을 담고, 사랑💜으로 만든 선물로 영원히 간직하고 싶어서 만들었어.
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Angel Focus On JUUN Forever</title>

    <link rel="stylesheet" href="style.css">
</head>

<body>

    <div class="container">

        <h1>Angel Focus On JUUN Forever</h1>

        <h2>주은과 함께한 추억 💜</h2>

        <img src="images/juun1.jpg" alt="JUUN">

        <p>
            A collection of memories, letters, and moments shared with JUUN.
        </p>

        <button>
            Enter
        </button>

    </div>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Angel Focus On JUUN Forever</title>

    <link rel="stylesheet" href="style.css">
</head>

<body>

    <div class="container">

        <h1>Angel Focus On JUUN Forever</h1>

        <h2>주은과 함께한 추억 💜</h2>

        <img src="images/juun1.jpg" alt="JUUN">

        <p>
            A collection of memories, letters, and moments shared with JUUN.
        </p>

        <button>
            Enter
        </button>

    </div>

</body>

</html>
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>主恩 Website 💜</title>
    <style>
        body {
            margin: 0;
            font-family: 'Arial', sans-serif;
            background-color: #f3e8ff; /* 淡紫色背景 */
        }

        header {
            background-color: #6a0dad; /* 深紫色 */
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 2em;
        }

        main {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            padding: 20px;
        }

        .photo-card {
            background-color: white;
            border-radius: 12px;
            margin: 15px;
            overflow: hidden;
            width: 250px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }

        .photo-card img {
            width: 100%;
            display: block;
        }

        .photo-card:hover {
            transform: scale(1.05);
        }

        footer {
            text-align: center;
            padding: 15px;
            background-color: #6a0dad;
            color: white;
        }
    </style>
</head>
<body>
    <header>
        주은 Website 💜
    </header>

    <main id="photo-gallery">
        <!-- 照片会在这里显示 -->
    </main>

    <footer>
        © 2026 主恩 Website
    </footer>

    <script>
        // 示例照片列表（后续可以换成联网获取）
        const photos = [
            'https://via.placeholder.com/250x300.png?text=JUUN+1',
            'https://via.placeholder.com/250x300.png?text=JUUN+2',
            'https://via.placeholder.com/250x300.png?text=JUUN+3'
        ];

        const gallery = document.getElementById('photo-gallery');

        photos.forEach(src => {
            const card = document.createElement('div');
            card.className = 'photo-card';

            const img = document.createElement('img');
            img.src = src;

            card.appendChild(img);
            gallery.appendChild(card);
        });
    </script>
</body>
</html>
