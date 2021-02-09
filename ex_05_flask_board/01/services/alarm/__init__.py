from services import app
from flask import request, session, render_template, redirect
from flask import session as flaskSession
from services.member import service as member_service
from util import authDecorator
from services.authority import service as authority_service