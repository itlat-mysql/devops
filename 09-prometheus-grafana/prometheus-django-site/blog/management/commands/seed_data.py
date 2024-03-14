from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import shutil
import os
from app import settings

from blog.models import Post


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **options):
        self.seed_users()
        self.seed_posts()
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))

    def seed_users(self):
        # Delete old users
        all_users = User.objects.all()
        for user in all_users:
            user.delete()

        # create new superuser
        User.objects.create_superuser('user', 'user@gmail.com', 'secret')

    def seed_posts(self):
        # Delete old posts
        all_posts = Post.objects.all()
        for post in all_posts:
            post.delete()

        user = User.objects.first()

        posts_items = [
    {
                'title': 'The Adventures of Pinocchio',
                'content' : """How it happened that Mastro Cherry, carpenter, found a piece of wood that wept and laughed like a child.

Centuries ago there lived—

“A king!” my little readers will say immediately.

No, children, you are mistaken. Once upon a time there was a piece of wood. It was not an expensive piece of wood. Far from it. Just a common block of firewood, one of those thick, solid logs that are put on the fire in winter to make cold rooms cozy and warm.

I do not know how this really happened, yet the fact remains that one fine day this piece of wood found itself in the shop of an old carpenter. His real name was Mastro Antonio, but everyone called him Mastro Cherry, for the tip of his nose was so round and red and shiny that it looked like a ripe cherry.

As soon as he saw that piece of wood, Mastro Cherry was filled with joy. Rubbing his hands together happily, he mumbled half to himself:

“This has come in the nick of time. I shall use it to make the leg of a table.”

He grasped the hatchet quickly to peel off the bark and shape the wood. But as he was about to give it the first blow, he stood still with arm uplifted, for he had heard a wee, little voice say in a beseeching tone: “Please be careful! Do not hit me so hard!”

What a look of surprise shone on Mastro Cherry’s face! His funny face became still funnier.""",
                'active': True,
                'image': 'pinocchio.jpg'
},
            {
                'title': 'Treasure Island',
                'content': """All of us had an ample share of the treasure and used it wisely or foolishly, according to our natures. Captain Smollett is now retired from the sea. Gray not only saved his money, but being suddenly smit with the desire to rise, also studied his profession, and he is now mate and part owner of a fine full-rigged ship, married besides, and the father of a family. As for Ben Gunn, he got a thousand pounds, which he spent or lost in three weeks, or to be more exact, in nineteen days, for he was back begging on the twentieth. Then he was given a lodge to keep, exactly as he had feared upon the island; and he still lives, a great favourite, though something of a butt, with the country boys, and a notable singer in church on Sundays and saints’ days.

Of Silver we have heard no more. That formidable seafaring man with one leg has at last gone clean out of my life; but I dare say he met his old Negress, and perhaps still lives in comfort with her and Captain Flint. It is to be hoped so, I suppose, for his chances of comfort in another world are very small.

The bar silver and the arms still lie, for all that I know, where Flint buried them; and certainly they shall lie there for me. Oxen and wain-ropes would not bring me back again to that accursed island; and the worst dreams that ever I have are when I hear the surf booming about its coasts or start upright in bed with the sharp voice of Captain Flint still ringing in my ears: “Pieces of eight! Pieces of eight!”'""",
                'active': True,
                'image': 'treasure-island.jpg'
            },
            {
                'title': 'Robinson Crusoe',
                'content': """I was born in the year 1632, in the city of York, of a good family, though not of that country, my father being a foreigner of Bremen, who settled first at Hull. He got a good estate by merchandise, and leaving off his trade, lived afterwards at York, from whence he had married my mother, whose relations were named Robinson, a very good family in that country, and from whom I was called Robinson Kreutznaer; but, by the usual corruption of words in England, we are now called—nay we call ourselves and write our name—Crusoe; and so my companions always called me.

I had two elder brothers, one of whom was lieutenant-colonel to an English regiment of foot in Flanders, formerly commanded by the famous Colonel Lockhart, and was killed at the battle near Dunkirk against the Spaniards. What became of my second brother I never knew, any more than my father or mother knew what became of me.

Being the third son of the family and not bred to any trade, my head began to be filled very early with rambling thoughts. My father, who was very ancient, had given me a competent share of learning, as far as house-education and a country free school generally go, and designed me for the law; but I would be satisfied with nothing but going to sea; and my inclination to this led me so strongly against the will, nay, the commands of my father, and against all the entreaties and persuasions of my mother and other friends, that there seemed to be something fatal in that propensity of nature, tending directly to the life of misery which was to befall me.""",
                'active': True,
                'image': 'robinson-crusoe.jpg',
            },
            {
                'title': 'Sherlock Holmes',
                'content': """“To the man who loves art for its own sake,” remarked Sherlock Holmes, tossing aside the advertisement sheet of The Daily Telegraph, “it is frequently in its least important and lowliest manifestations that the keenest pleasure is to be derived. It is pleasant to me to observe, Watson, that you have so far grasped this truth that in these little records of our cases which you have been good enough to draw up, and, I am bound to say, occasionally to embellish, you have given prominence not so much to the many causes célèbres and sensational trials in which I have figured but rather to those incidents which may have been trivial in themselves, but which have given room for those faculties of deduction and of logical synthesis which I have made my special province.”

“And yet,” said I, smiling, “I cannot quite hold myself absolved from the charge of sensationalism which has been urged against my records.”

“You have erred, perhaps,” he observed, taking up a glowing cinder with the tongs and lighting with it the long cherry-wood pipe which was wont to replace his clay when he was in a disputatious rather than a meditative mood—“you have erred perhaps in attempting to put colour and life into each of your statements instead of confining yourself to the task of placing upon record that severe reasoning from cause to effect which is really the only notable feature about the thing.”""",
                'active': True,
                'image': 'sherlock-holmes.jpg'
            },
            {
                'title': 'Tom Sawyer',
                'content': """The old lady pulled her spectacles down and looked over them about the room; then she put them up and looked out under them. She seldom or never looked _through_ them for so small a thing as a boy; they were her state pair, the pride of her heart, and were built for "style," not service--she could have seen through a pair of stove-lids just as well. She looked perplexed for a moment, and then said, not fiercely, but still loud enough for the furniture to hear:

"Well, I lay if I get hold of you I\'ll--"

She did not finish, for by this time she was bending down and punching under the bed with the broom, and so she needed breath to punctuate the punches with. She resurrected nothing but the cat.""",
                'active': True,
                'image': 'tom-sawyer.jpg'
            },
            {
                'title': 'The Jungle Book',
                'content': """It was seven o’clock of a very warm evening in the Seeonee hills when Father Wolf woke up from his day’s rest, scratched himself, yawned, and spread out his paws one after the other to get rid of the sleepy feeling in their tips. Mother Wolf lay with her big gray nose dropped across her four tumbling, squealing cubs, and the moon shone into the mouth of the cave where they all lived. “Augrh!” said Father Wolf. “It is time to hunt again.” He was going to spring down hill when a little shadow with a bushy tail crossed the threshold and whined: “Good luck go with you, O Chief of the Wolves. And good luck and strong white teeth go with noble children that they may never forget the hungry in this world.”

                It was the jackal—Tabaqui, the Dish-licker—and the wolves of India despise Tabaqui because he runs about making mischief, and telling tales, and eating rags and pieces of leather from the village rubbish-heaps. But they are afraid of him too, because Tabaqui, more than anyone else in the jungle, is apt to go mad, and then he forgets that he was ever afraid of anyone, and runs through the forest biting everything in his way. Even the tiger runs and hides when little Tabaqui goes mad, for madness is the most disgraceful thing that can overtake a wild creature. We call it hydrophobia, but they call it dewanee—the madness—and run.

                “Enter, then, and look,” said Father Wolf stiffly, “but there is no food here.”""",
                'active': True,
                'image': 'jungle-book.jpg'
            },
            {
                'title': 'Robin Hood',
                'content': """In merry England in the time of old, when good King Henry the Second ruled the land, there lived within the green glades of Sherwood Forest, near Nottingham Town, a famous outlaw whose name was Robin Hood. No archer ever lived that could speed a gray goose shaft with such skill and cunning as his, nor were there ever such yeomen as the sevenscore merry men that roamed with him through the greenwood shades. Right merrily they dwelled within the depths of Sherwood Forest, suffering neither care nor want, but passing the time in merry games of archery or bouts of cudgel play, living upon the King\'s venison, washed down with draughts of ale of October brewing.

    Not only Robin himself but all the band were outlaws and dwelled apart from other men, yet they were beloved by the country people round about, for no one ever came to jolly Robin for help in time of need and went away again with an empty fist.

And now I will tell how it came about that Robin Hood fell afoul of the law.""",
                'active': True,
                'image': 'robin-hood.jpg'
            },
            {
                'title': 'Twenty Thousand Leagues under the Sea',
                'content': """The year 1866 was signalised by a remarkable incident, a mysterious and puzzling phenomenon, which doubtless no one has yet forgotten. Not to mention rumours which agitated the maritime population and excited the public mind, even in the interior of continents, seafaring men were particularly excited. Merchants, common sailors, captains of vessels, skippers, both of Europe and America, naval officers of all countries, and the Governments of several states on the two continents, were deeply interested in the matter.

For some time past, vessels had been met by “an enormous thing,” a long object, spindle-shaped, occasionally phosphorescent, and infinitely larger and more rapid in its movements than a whale.

The facts relating to this apparition (entered in various log-books) agreed in most respects as to the shape of the object or creature in question, the untiring rapidity of its movements, its surprising power of locomotion, and the peculiar life with which it seemed endowed.""",
                'active': True,
                'image': '20000.jpg'
            },
            {
                'title': 'The Wonderful Wizard of Oz',
                'content': """Dorothy lived in the midst of the great Kansas prairies, with Uncle Henry, who was a farmer, and Aunt Em, who was the farmer’s wife. Their house was small, for the lumber to build it had to be carried by wagon many miles. There were four walls, a floor and a roof, which made one room; and this room contained a rusty looking cookstove, a cupboard for the dishes, a table, three or four chairs, and the beds. Uncle Henry and Aunt Em had a big bed in one corner, and Dorothy a little bed in another corner. There was no garret at all, and no cellar—except a small hole dug in the ground, called a cyclone cellar, where the family could go in case one of those great whirlwinds arose, mighty enough to crush any building in its path. It was reached by a trap door in the middle of the floor, from which a ladder led down into the small, dark hole.

When Dorothy stood in the doorway and looked around, she could see nothing but the great gray prairie on every side. Not a tree nor a house broke the broad sweep of flat country that reached to the edge of the sky in all directions. The sun had baked the plowed land into a gray mass, with little cracks running through it. Even the grass was not green, for the sun had burned the tops of the long blades until they were the same gray color to be seen everywhere. Once the house had been painted, but the sun blistered the paint and the rains washed it away, and now the house was as dull and gray as everything else.

When Aunt Em came there to live she was a young, pretty wife. The sun and wind had changed her, too. They had taken the sparkle from her eyes and left them a sober gray; they had taken the red from her cheeks and lips, and they were gray also. She was thin and gaunt, and never smiled now. When Dorothy, who was an orphan, first came to her, Aunt Em had been so startled by the child’s laughter that she would scream and press her hand upon her heart whenever Dorothy’s merry voice reached her ears; and she still looked at the little girl with wonder that she could find anything to laugh at.""",
                'active': True,
                'image': 'wizard-of-oz.jpg'
            },
            {
                'title': 'White Fang',
                'content': """Dark spruce forest frowned on either side the frozen waterway. The trees had been stripped by a recent wind of their white covering of frost, and they seemed to lean towards each other, black and ominous, in the fading light. A vast silence reigned over the land. The land itself was a desolation, lifeless, without movement, so lone and cold that the spirit of it was not even that of sadness. There was a hint in it of laughter, but of a laughter more terrible than any sadness—a laughter that was mirthless as the smile of the sphinx, a laughter cold as the frost and partaking of the grimness of infallibility. It was the masterful and incommunicable wisdom of eternity laughing at the futility of life and the effort of life. It was the Wild, the savage, frozen-hearted Northland Wild.

But there was life, abroad in the land and defiant. Down the frozen waterway toiled a string of wolfish dogs. Their bristly fur was rimed with frost. Their breath froze in the air as it left their mouths, spouting forth in spumes of vapour that settled upon the hair of their bodies and formed into crystals of frost. Leather harness was on the dogs, and leather traces attached them to a sled which dragged along behind. The sled was without runners. It was made of stout birch-bark, and its full surface rested on the snow. The front end of the sled was turned up, like a scroll, in order to force down and under the bore of soft snow that surged like a wave before it. On the sled, securely lashed, was a long and narrow oblong box. There were other things on the sled—blankets, an axe, and a coffee-pot and frying-pan; but prominent, occupying most of the space, was the long and narrow oblong box.

In advance of the dogs, on wide snowshoes, toiled a man. At the rear of the sled toiled a second man. On the sled, in the box, lay a third man whose toil was over,—a man whom the Wild had conquered and beaten down until he would never move nor struggle again. It is not the way of the Wild to like movement. Life is an offence to it, for life is movement; and the Wild aims always to destroy movement. It freezes the water to prevent it running to the sea; it drives the sap out of the trees till they are frozen to their mighty hearts; and most ferociously and terribly of all does the Wild harry and crush into submission man—man who is the most restless of life, ever in revolt against the dictum that all movement must in the end come to the cessation of movement.""",
                'active': True,
                'image': 'white-fang.jpg'
            },
        ]

        for post_item in posts_items:
            Post(
                title=post_item.get('title'),
                content=post_item.get('content'),
                image=post_item.get('image'),
                active=post_item.get('active'),
                admin=user
            ).save()

            shutil.copy2(os.path.join(
                settings.BASE_DIR, 'install-data', post_item.get('image')),
                os.path.join(settings.MEDIA_ROOT, post_item.get('image'))
            )
