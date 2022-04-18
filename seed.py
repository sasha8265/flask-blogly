from models import User, Post, Tag, db
from app import app

# Create all tables
db.drop_all()
db.create_all()


"""Make some users"""

sasha = User(first_name="Sasha", last_name="Czerniawski", image_url="https://scontent-lga3-2.xx.fbcdn.net/v/t39.30808-6/242364092_10225164627599618_3179410832309430575_n.jpg?stp=dst-jpg_s640x640&_nc_cat=108&ccb=1-5&_nc_sid=730e14&_nc_ohc=hcatq9--FW0AX9FLOsJ&_nc_ht=scontent-lga3-2.xx&oh=00_AT_4b_DZJVvi55ZwQIuDDk6P5lvAAmRNZEDOij0FbIoIkQ&oe=625EDF09")
andrea = User(first_name="Andrea", last_name="Michelcic", image_url="https://scontent-lga3-2.xx.fbcdn.net/v/t39.30808-6/277732848_3101388643521768_3868561096895745623_n.jpg?_nc_cat=104&ccb=1-5&_nc_sid=730e14&_nc_ohc=8Uydkxpqv4cAX98dTHn&_nc_ht=scontent-lga3-2.xx&oh=00_AT921HdxtjTqtVBtITLhIY8Uqi8Jkit2xx6XLs61ioraQg&oe=625F97AB")
jay = User(first_name="Jay", last_name="Quinn", image_url="https://scontent-lga3-2.xx.fbcdn.net/v/t1.18169-9/8387_10103407417519824_8683212659811699755_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=Macrnbr4AMIAX_H2w3I&_nc_ht=scontent-lga3-2.xx&oh=00_AT-tWB-Fb5pu2dw02RRSsMGAbsU7RguGcnGI3EfZu_PPCQ&oe=627DC651")

db.session.add_all([sasha, andrea, jay])
db.session.commit()



"""Make some posts"""

p1 = Post(title="Best Ever Bacon Ipsum", content="Bacon ipsum dolor amet fugiat jowl in brisket minim sint, kielbasa ipsum ut eiusmod kevin andouille turkey aliquip. Magna in filet mignon quis in swine enim, salami meatloaf beef ribs turkey fatback drumstick ham hock rump. Picanha lorem est ullamco andouille reprehenderit, pastrami chislic. Porchetta tongue in, sausage tri-tip aute reprehenderit laborum eu tenderloin flank beef in strip steak magna. Duis pork loin ham est laboris. Mollit et ad, cow est beef dolor adipisicing flank do chislic jerky. In eiusmod ea minim, kevin andouille magna occaecat dolore laborum short loin adipisicing. Hamburger est in velit proident landjaeger. Et sirloin qui anim shoulder eu beef ribs culpa do deserunt ham.", user_id=3)
p2 = Post(title="Some Coffee Ipsum", content="Arabica Acerbic Affogato Aftertaste Aged Americano And Aroma, bar panna so Barista cortado trifecta extraction, skinny aftertaste filter java cultivar cinnamon. Mazagran trade Barista french and Acerbic acerbic Aged milk cinnamon origin carajillo, mountain coffee roast mug wings Bar single viennese pumpkin go pot, dripper crema flavour mocha At bar sit medium au breve. Espresso Brewed Blue iced Americano robust whipped, bar percolator grounds go saucer robusta, Au shop Affogato Bar aged coffee, Barista blue strong origin aftertaste. Blue skinny coffee breve Brewed acerbic, siphon steamed And foam, qui Arabica ut latte. Go brewed At aftertaste sweet cinnamon caffeine rich strong caramelization Aftertaste, Body roast body frappuccino Beans extraction sit americano Aroma.", user_id=1)
p3 = Post(title="Cupcake Ipsum", content="Cupcake ipsum dolor sit amet candy canes pie muffin pudding. Cupcake oat cake carrot cake marshmallow toffee sweet roll shortbread. Pie marzipan cake powder gingerbread halvah cheesecake cake jelly-o. Pie lollipop candy canes cake apple pie. Pastry powder apple pie chocolate cake bear claw gingerbread donut croissant bonbon. Cake brownie candy canes pie jujubes tiramisu. Cupcake donut cotton candy jujubes tiramisu chupa chups. Fruitcake oat cake cotton candy toffee ice cream marzipan. Jelly-o cookie marzipan dragée pudding. Candy canes oat cake gummi bears chupa chups ice cream shortbread liquorice. Halvah croissant chocolate cake biscuit soufflé soufflé sweet. Sesame snaps jujubes donut gummies cake cotton candy pastry toffee wafer. Candy chocolate cake lollipop pudding chupa chups candy oat cake.", user_id=2)

db.session.add_all([p1, p2, p3])
db.session.commit()


"""Create some tags"""

t1 = Tag(tag_name="food")
t2 = Tag(tag_name="nonesense")
t3 = Tag(tag_name="genius")

db.session.add_all([t1, t2, t3])
db.session.commit()