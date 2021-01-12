from services import app
from services.member import service as member_service

@app.route('/test/member')
def test_member():
  member_service.test_member_service()
  return "test_member..."