from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 韩语翻译数据库
translation_database = {
    # 常见中文词汇
    "我爱你": "사랑해요",
    "想你": "보고 싶어요",
    "我想你": "보고 싶어요",
    "永远": "영원히",
    "永远爱你": "영원히 사랑해요",
    "加油": "파이팅!",
    "祝贺": "축하해요",
    "恭喜": "축하해요",
    "生日快乐": "생일 축하해요",
    "好开心": "정말 행복해요",
    "好可爱": "정말 귀여워요",
    "好漂亮": "정말 예뻐요",
    "好帅": "정말 멋있어요",
    "我们会见面的": "우리 만날 거예요",
    "快见面吧": "빨리 만나자",
    "我们快点见面吧": "우리 빨리 만나자",
    "主恩": "주은",
    "小恩": "주은아",
    "出道": "데뷔",
    "演唱会": "콘서트",
    "粉丝见面会": "팬미팅",
    "粉丝": "팬",
    "见面": "만나다",
    "幸福": "행복",
    "爱": "사랑",
    "支持": "응원",
    "天使": "천사",
    "宝贝": "보물",
    "舞台": "무대",
    "表演": "공연",
    "感动": "감동",
    "喜欢": "좋아하다",
    "谢谢": "감사해요",
    "今天": "오늘",
    "明天": "내일",
    "希望你幸福": "행복하길 바래요",
    "我会支持你": "응원할게요",
    "谢谢": "감사해요",
    "对不起": "미안해요",
    "没关系": "괜찮아요",
    "你好": "안녕하세요",
    "再见": "안녕히 가세요",
    "晚安": "잘 자요",
    "早上好": "좋은 아침",
    
    # 短语和句子
    "此时此刻我很想你哦小恩": "지금 이 순간 주은아 많이 보고 싶어요",
    "我们小恩出道啦": "우리 주은 데뷔했어",
    "希望她永远幸福": "그녀가 영원히 행복하길 바래요",
    "永远被爱": "영원히 사랑받아요",
    "快乐地享受舞台": "즐겁게 무대 즐겨요",
    "Angel focus on JUUN forever": "Angel은 영원히 주은을 응원해요",
    "要一直健康": "항상 건강해야 해요",
    "要一直快乐": "항상 행복해야 해요",
    "属于她们和我们之间的第一场FM": "그들과 우리 사이의 첫 번째 FM",
    "我们主恩突然就长大啦": "우리 주은이 어느새 컸어",
    
    # 英文词汇
    "love": "사랑",
    "forever": "영원히",
    "thank you": "감사해요",
    "sorry": "미안해요",
    "happy": "행복해",
    "sad": "슬퍼",
    "good": "좋아",
    "bad": "나빠",
    "hello": "안녕",
    "bye": "잘 가",
    "see you": "再见",
    "miss you": "보고 싶어요",
    "excited": "신나",
    "crush": "짝사랑",
    "baby": "베이비",
    "beautiful": "아름다워",
    "amazing": "놀라워",
    "wonderful": "멋져",
    "perfect": "완벽해"
}

@app.route('/api/translate', methods=['POST'])
def translate():
    """
    翻译API - 将中文/英文翻译成韩语
    
    请求格式:
    {
        "text": "要翻译的文本"
    }
    
    响应格式:
    {
        "original": "原始文本",
        "translated": "翻译后的文本",
        "success": true
    }
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({
                'original': '',
                'translated': '',
                'success': False,
                'error': 'No text provided'
            }), 400
        
        # 逐词翻译
        result = text
        for original, translated in translation_database.items():
            result = result.replace(original, translated)
        
        return jsonify({
            'original': text,
            'translated': result,
            'success': True
        })
    
    except Exception as e:
        return jsonify({
            'original': '',
            'translated': '',
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/translate-database', methods=['GET'])
def get_database():
    """
    获取翻译数据库的全部内容
    """
    return jsonify({
        'database': translation_database,
        'count': len(translation_database),
        'success': True
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    健康检查接口
    """
    return jsonify({
        'status': 'healthy',
        'service': 'Korean Translation API',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)