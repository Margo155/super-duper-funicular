from pathlib import Path
import json, re, itertools, hashlib

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT
sections = json.loads((ROOT/'planning/scenes_source.json').read_text())
camera_rows = [
 ['Крупно ручка и открывающаяся дверь; лёгкий отъезд раскрывает преграду.', 'Внутри комнаты на уровне лица героя; прохожие дают передний план снаружи.', 'Плавный боковой переход к разрезу, раскрывающему старую и новую отметки.'],
 ['Низкий сопровождающий проезд за стопой к луже.', 'Средний боковой план: виден намеренный выход стопы из застрявшего ботинка.', 'Общий план устойчивой доски; сохраняем непрерывность восстановления обуви.'],
 ['Средний план: доска, герой и растущая лужа в глубине.', 'Боковой dolly по условному грунтовому разрезу.', 'Подъём к условной карте района; одинаковая точка стока связывает планы.'],
 ['Предметный план настольного желоба, небольшой параллакс.', 'Профиль модели показывает направление наклона и воды.', 'Сопоставление модели с разрезом улицы, без полёта через реальные стены.'],
 ['План сверху на карту и типографическое имя инженера.', 'Боковая схема этапов: труба, насыпь, покрытие.', 'Приближение к пальцу героя и линии через нарисованную дверь.'],
 ['Общий план с фиксированной камерой для явного сжатия времени.', 'Повтор камерного ракурса первой двери; разница высот очевидна.', 'Средний план с обеими стопами на временных ступенях.'],
 ['Низкий ракурс от порога на высокую улицу.', 'Средний план героя и явно условной схемы мысли.', 'Предметный низкий ракурс через домкрат на дом.'],
 ['Макро резьбы с медленным боковым проездом.', 'Условный разрез винта и гайки с фиксированной опорой.', 'Средний план героя у модели: обе руки, груз и край стола читаются.'],
 ['Схема распределения опор в плане; без имитации точного расчёта.', 'Короткий проезд через условный разрез вдоль несущих балок.', 'Средний план героя на внешней площадке; взгляд следует по опорам.'],
 ['Средний план бригадира и ожидающих рабочих.', 'Крупные планы согласованных небольших движений рукояток.', 'Небольшой боковой проезд к рейке героя и контрольной отметке.'],
 ['Макро зазора и риски, не выдавать увеличение за реальную скорость.', 'Общий фронтальный план дома и отдельных корней улицы.', 'Внутренняя камера привязана к комнате; за окном меняется высота.'],
 ['Средний план героя с высоким тротуаром на втором плане.', 'Через плечо на проверку уровня и шкалы.', 'Боковой план всего дома во время очередного малого подъёма.'],
 ['Фиксированный общий план временного монтажа с изменением теней.', 'Боковой проезд вдоль разреза строящегося основания.', 'Средний план журнала и высотной отметки с героем рядом.'],
 ['Широкий план отдельного исторического квартала с подписью.', 'Разрез квартала, модульные опоры и читаемое число 6,000.', 'Боковой проезд вдоль витрин; склейка по форме балки обратно к дому A.'],
 ['Макро совпадающих отметок, затем жест бригадира.', 'Спокойный разрез передачи нагрузки на новое основание.', 'Широкий неполный обход дома, без неожиданного изменения его фасада.'],
 ['Общий разрез: старый грунт, трубы, насыпь, улица, дом.', 'Боковой проезд по соседним участкам с разными состояниями.', 'Сопоставление дверей A и B на постоянных местах.'],
 ['Макро первых капель и движения небольшой струи.', 'Следим за водой в условном разрезе до выхода.', 'Короткий отъезд к графической карте с рекой; без зелёной магической очистки.'],
 ['Точное повторение композиции комнаты из начала.', 'Крупно старый грязный след; обувь героя остаётся надетой.', 'Медленный push к окну и герою, читаемый новый уровень улицы.'],
 ['MATCH OPENING: тот же объектив и камера относительно House A.', 'Отъезд перед героем, позволяющий видеть последовательные шаги.', 'Общий подъём/отъезд раскрывает новый цоколь и улицу.'],
 ['Ракурс над краем тротуара к руке соседа с ботинком.', 'Средний план героя: берёт рейку и поворачивается к соседу.', 'Общий план двух домов, небольшое движение камеры и живой финал.'],
]

def words(s): return len(s.split())
def split_three(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    candidates = []
    for a,b in itertools.combinations(range(1,len(sentences)),2):
        groups = [' '.join(sentences[:a]),' '.join(sentences[a:b]),' '.join(sentences[b:])]
        counts = [words(g) for g in groups]
        cost = sum((c-words(text)/3)**2 for c in counts)
        candidates.append((cost,groups))
    if not candidates: raise ValueError('Need at least three sentences per scene')
    return min(candidates,key=lambda x:x[0])[1]

voice = '\n\n'.join(s['en'] for s in sections)
translation = '\n\n'.join(s['ru'] for s in sections)
(PKG/'audio/VOICEOVER_EN.txt').write_text(voice+'\n')
(PKG/'audio/VOICEOVER_RU_REFERENCE.txt').write_text(translation+'\n')

shots=[]; scene_plan=[]; pauses=[]; caption_events=[]; caption_index=1
for s in sections:
    sid=s['id']; parts=split_three(s['en']); scene_start=(sid-1)*900
    spare=900-words(s['en'])*12
    if spare<0:raise ValueError('Scene narration exceeds 30 seconds at 150 wpm')
    cursor=scene_start
    for k,part in enumerate(parts):
        extra=spare//3+(1 if k<spare%3 else 0)
        length=words(part)*12+extra
        sf=cursor;ef=cursor+length;lead=extra//2;tail=extra-lead
        vs=sf+lead;ve=vs+words(part)*12
        n=(sid-1)*3+k+1
        lighting='Мягкий естественный свет; согласованные контактные тени.'
        if sid in (2,3):lighting='Пасмурный свет после дождя; читаемые грязь и силуэт.'
        if sid==13:lighting='Смена света только как явно обозначенное сжатие времени.'
        if sid==17:lighting='Рассеянный дождевой свет; мягкие тени.'
        if sid in (19,20):lighting='Тёплый свет после дождя, без скачка погоды внутри плана.'
        shot={'id':f'S{n:03d}','scene':sid,'start_frame':sf,'end_frame_exclusive':ef,
              'start_s':sf/30,'end_s':ef/30,'frames':length,'voice_start_frame':vs,
              'voice_end_frame_exclusive':ve,'voiceover':part,'action_ru':s['actions'][k],
              'camera_ru':camera_rows[sid-1][k],'lighting_ru':lighting,'state':s['state'],
              'historical_status':s['status'],'shoe_removal_planned':n in (4,5,6),
              'control_frame':(sf+ef)//2}
        shots.append(shot)
        pauses.extend([{'start_frame':sf,'end_frame_exclusive':vs,'shot':shot['id'],'kind':'action_lead'},
                       {'start_frame':ve,'end_frame_exclusive':ef,'shot':shot['id'],'kind':'action_tail'}])
        ws=part.split();groups=[];g=[]
        for w in ws:
            if g and (len(g)==4 or len(' '.join(g+[w]))>38):groups.append(g);g=[]
            g.append(w)
            if re.search(r'[.!?]$',w):groups.append(g);g=[]
        if g:groups.append(g)
        f=vs
        for group in groups:
            end=f+len(group)*12
            caption_events.append({'index':caption_index,'start_frame':f,'end_frame_exclusive':end,
                                   'text':' '.join(group),'shot':shot['id'],'status':'DRAFT_NOT_AUDIO_ALIGNED'})
            caption_index+=1;f=end
        assert f==ve
        cursor=ef
    assert cursor==sid*900
    scene_plan.append({**s,'start_frame':scene_start,'end_frame_exclusive':sid*900,
                       'words':words(s['en']),'planned_voice_s':words(s['en'])*.4,
                       'planned_action_s':spare/30})

def stamp(frame):
    ms=round(frame/30*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
def clock(frame):
    seconds=frame/30;return f'{int(seconds)//60:02}:{seconds%60:06.3f}'

(PKG/'timeline.json').write_text(json.dumps({'status':'DRAFT_UNTIL_REAL_AUDIO_ALIGNMENT','fps':30,
 'duration_seconds':600,'frames':18000,'planned_wpm':150,'spoken_words':words(voice),
 'planned_action_seconds':76,'scenes':scene_plan},ensure_ascii=False,indent=2)+'\n')
(PKG/'shot_manifest.json').write_text(json.dumps({'fps':30,'duration_seconds':600,'shots':shots},ensure_ascii=False,indent=2)+'\n')
(PKG/'audio/pause_plan.json').write_text(json.dumps({'status':'DRAFT_ACTION_SOUND_BEATS_NOT_EMPTY_PADDING',
 'fps':30,'total_action_seconds':sum(p['end_frame_exclusive']-p['start_frame'] for p in pauses)/30,
 'events':pauses},ensure_ascii=False,indent=2)+'\n')
(PKG/'subtitles/caption_plan.json').write_text(json.dumps({'status':'DRAFT_NOT_AUDIO_ALIGNED','fps':30,
 'captions':caption_events},ensure_ascii=False,indent=2)+'\n')
(PKG/'subtitles/LONG_001_DRAFT.srt').write_text('\n\n'.join(
 f"{c['index']}\n{stamp(c['start_frame'])} --> {stamp(c['end_frame_exclusive'])}\n{c['text']}" for c in caption_events)+'\n')

script=['# Город, который пришлось поднять\n', '**The City They Had to Lift — Oddplot Long 001**\n',
 'Полный сценарий горизонтального десятиминутного фильма. 20 сцен, 60 планов. 1310 произносимых английских слов; расчёт при 150 словах/мин и 76 секундах действий даёт 600 секунд. Это расчётная сетка, не длительность записанного голоса. Итоговый фильм должен содержать ровно 18000 кадров при 30 fps.\n',
 'Один английский рассказчик; герой действует без разговорных реплик. Русский перевод служит для согласования и постановки. Временные границы сцен предварительные до записи речи.\n',
 'Историческая основа: изменение уровней улиц и зданий Чикаго в XIX веке. Герой, его дом и бытовые события вымышлены. Сжатие реальных работ во времени обозначено.\n']
for s in scene_plan:
    script += [f"## {s['id']:02}. {clock(s['start_frame'])}–{clock(s['end_frame_exclusive'])} — {s['title_ru']}\n",
               '**На экране:** '+' '.join(s['actions'])+'\n',
               '**English voiceover:**\n\n'+s['en']+'\n',
               '**Русский перевод:**\n\n'+s['ru']+'\n',
               f"Плановая речь: {s['planned_voice_s']:.1f} с; действия и звук без речи: {s['planned_action_s']:.1f} с.\n"]
script += ['## Производственные примечания\n',
 'Речь читается из audio/VOICEOVER_EN.txt без заголовков, таймкодов и постановочных указаний. Перевод и авторские действия не озвучиваются. В начале коротко обозначить animated story inspired by Chicago; в сценах моделей и монтажа использовать поясняющие подписи.\n',
 'Подробные ракурсы, свет и действия — STORYBOARD_60_SHOTS.md. Источники и границы вымысла — HISTORICAL_FACTS_AND_SOURCES.md. Проверки и исправления обуви из V3 — CONTINUITY_BIBLE.md и QA_CHECKLIST.md.\n']
(PKG/'SCRIPT_EN_RU.md').write_text('\n'.join(script))

story=['# Раскадровка: 60 планов / 10 минут\n',
 '16:9, 1920×1080, 30 fps. Диапазоны кадров: начало включительно, конец исключительно. Сумма — 18000 кадров. Сетка пока не выровнена по реальному голосу; при переносе границ сохранить весь текст и итоговые 600 секунд.\n']
for sh in shots:
    story += [f"## {sh['id']} · сцена {sh['scene']:02} · {clock(sh['start_frame'])}–{clock(sh['end_frame_exclusive'])}\n",
              f"Кадры {sh['start_frame']}–{sh['end_frame_exclusive']-1}; {sh['frames']/30:.3f} с. Состояние: {sh['state']}.\n",
              '**Действие:** '+sh['action_ru']+'\n', '**Камера:** '+sh['camera_ru']+'\n',
              '**Свет:** '+sh['lighting_ru']+'\n', '**Voiceover:** '+sh['voiceover']+'\n',
              f"Плановое окно речи: {clock(sh['voice_start_frame'])}–{clock(sh['voice_end_frame_exclusive'])}. Остаток занят действием/звуком.\n"]
    if sh['shoe_removal_planned']:story += ['**Обувь:** запланированный комический эпизод, непрерывно показать снятие, извлечение и надевание ботинка. После S006 нормальная связь ноги и обуви восстановлена.\n']
story += ['## Склейки и качество\n',
 'Ракурс меняется ради нового действия, масштаба или объяснения. Чистые склейки по движению, match cut первой/последней двери, мотивированные переходы к разрезу. Не заменять фильм последовательностью неподвижных изображений. Движение камеры должно менять пространственные отношения объектов.\n',
 'Все паузы заполняются предусмотренными жестами, проверками, перемещениями и звуком среды. Не нужны одинаковые 10-секундные zoom на каждом плане. Свет меняется во временном монтаже или при переходе погоды, а не случайно внутри непрерывного действия.\n']
(PKG/'STORYBOARD_60_SHOTS.md').write_text('\n'.join(story))
print(json.dumps({'scenes':len(sections),'shots':len(shots),'spoken_words':words(voice),
 'action_seconds':sum(p['end_frame_exclusive']-p['start_frame'] for p in pauses)/30,
 'caption_events':len(caption_events),'frames':shots[-1]['end_frame_exclusive'],
 'voice_sha256':hashlib.sha256(voice.encode()).hexdigest()},ensure_ascii=False))
