from flask import Flask, request, send_file, jsonify
from werkzeug.utils import secure_filename
from image_processing import process_image, convert_to_color  # 이미지 처리 함수를 임포트

app = Flask(__name__)

# 이미지 업로드 및 처리 엔드포인트
@app.route('/upload_and_process', methods=['POST'])
def upload_and_process_image():
    f = request.files['image']
    f.save(secure_filename(f.filename))

    # 이미지 처리 함수 호출
    processed_image = process_image(secure_filename(f.filename))

    # 처리된 이미지를 임시 파일로 저장
    processed_image_path = 'processed_image.jpg'
    processed_image.save(processed_image_path)

    # 처리된 이미지를 클라이언트에 반환
    return send_file(processed_image_path, as_attachment=True)

# 이미지 가져오기 및 반환 엔드포인트
@app.route('/get_processed_image', methods=['GET'])
def get_processed_image():
    # 이미지 처리 서비스에서 이미지 가져오는 코드
    processed_image = get_processed_image_from_service()

    # 이미지를 클라이언트에 반환
    return send_file(processed_image, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host='165.229.229.173', port=5000)
