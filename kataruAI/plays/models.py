from django.db import models
from .models import *
from accounts.models import *
from scenarios.models import *
# Create your models here.

class Play(models.Model):
    class Status(models.TextChoices):
        PLAYING = 'PLAYING',  'プレイ中'
        CLEARED = 'CLEARED',  'クリア済'
        FAILED = 'FAILED',  '失敗'
        ABORTED = 'ABORTED', '中断'
    user = models.ForeignKey(
        User,
        verbose_name="ユーザー",
        on_delete=models.PROTECT
    )
    scenario = models.ForeignKey(
        Scenario,
        verbose_name="シナリオ",
        on_delete=models.PROTECT
    )
    status = models.CharField(
        verbose_name="状態",
        max_length=10,
        choices=Status.choices,
        default=Status.PLAYING,
    ) 
    mood = models.PositiveSmallIntegerField(
        verbose_name="機嫌",
        default=50,
    )
    supicion = models.PositiveSmallIntegerField(
        verbose_name="疑い",
        default=50
    )
    undestanding = models.PositiveSmallIntegerField(
        verbose_name="理解度",
        default=50,
    ) 
    turn_limit = models.PositiveSmallIntegerField(
        verbose_name="ターン上限",
    )
    turns_used = models.PositiveSmallIntegerField(
        verbose_name="使用ターン数",
        default=0
    ) 
    score = models.PositiveIntegerField(
        verbose_name="スコア",
        null=True,
        blank=True
    ) 
    save_chat_log = models.BooleanField(
        verbose_name="会話ログの保存有無",
        null=True,
        blank=True
    )
    started_at = models.DateTimeField(
        verbose_name="開始日時",
        auto_now_add=True
    )
    finished_at = models.DateTimeField(
        verbose_name="終了日時",
        null=True,
        blank=True,
    )

class PlayTurn(models.Model):
    play = models.ForeignKey(
        Play,
        verbose_name="プレイ",
        on_delete=models.CASCADE,
        related_name="turns"
    )
    turn_no = models.PositiveSmallIntegerField(
        verbose_name="ターン番号",
    )
    user_message = models.TextField(
        verbose_name="ユーザーの発言",
        max_length=120,
        null=True,
        blank=True
    )
    ai_reply = models.TextField(
        verbose_name="AIの返答",
        null=True,
        blank=True
    )
    delta_mood = models.SmallIntegerField(
        verbose_name="機嫌の増減",
        # ±13に丸めた後(マイナスあり)
    )
    delta_suspicion = models.SmallIntegerField(
        verbose_name="疑いの増減",
        # ±13に丸めた後(マイナスあり)
    )
    delta_unserstanding = models.SmallIntegerField(
        verbose_name="理解度の増減",
        # ±13に丸めた後(マイナスあり)
    )
    mood_after = models.PositiveIntegerField(
        # ターン後の値
        verbose_name="ターン後の機嫌",
    )
    suspicion_after = models.PositiveIntegerField(
        # ターン後の値
        verbose_name="ターン後の疑い",
    )
    understanding_after = models.PositiveIntegerField(
        # ターン後の値
        verbose_name="ターン後の理解度",
    )
    state_text = models.TextField(
        verbose_name="今の様子",
        max_length="100"
    )
    expression = models.TextField(
        verbose_name="表情",
        max_length="100"
    )
    reason = models.TextField(
        # 解説用のデータ
        verbose_name="表情が変わった理由",
        blank=True,
        null=True,
    )
    create_at = models.DateTimeField(
        verbose_name="記録日時",
        auto_now_add=True
    )
