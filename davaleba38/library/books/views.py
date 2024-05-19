from django.shortcuts import render, redirect


books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald,", "img_link": "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1689690358-screenshot-2023-07-18-at-15-25-38-64b6a0e73c9e9.png?crop=0.9596199524940617xw:1xh;center,top&resize=980:*", "description": "Short but oh-so-sweet, F. Scott Fitzgerald's masterpiece has become synonymous with the Roaring Twenties and the death of the so-called American Dream. A modern tragedy, it charts the fall of Jay Gatsby, a newly minted millionaire, as he attempts to win back the love of his former sweetheart Daisy Buchanan, now married to another wealthy man. In his obsessive quest for wealth and status, as symbolised by Daisy, he neglects to see her true nature – which ultimately causes his downfall. Ironically, The Great Gatsby was not as much of a success as Fitzgerald's previous novels, This Side of Paradise and The Beautiful and the Damned. It was only posthumously that the book rose to prominence, and was even distributed freely amongst WWII American troops overseas to boost cultural morale. These days, it's regarded as Fitzgerland's magnum opus."},
    {"id": 2, "title": "To Kill A Mockingbird", "author": "Harper Lee", "img_link": "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1689690065-screenshot-2023-07-18-at-15-20-40-64b69fbe354c8.png?crop=0.9361046959199384xw:1xh;center,top&resize=980:*", "description": "Harper Lee's classic tale set in 1930s Alabama is perhaps the seminal text on racial tensions in the Deep South. The story follows the white lawyer Atticus Finch as he attempts to save the life of Tom Robinson, a Black man falsely accused of raping a white woman. The innocence of the narrator – Finch's six-year-old daughter, Scout – only serves to highlight the unfairness and incomprehensibility of the situation. A true American classic, To Kill A Mockingbird approaches the thorny issue of racism in the USA with humour, warmth and compassion, making it widely recognised as one of the greatest books of the twentieth century. Lee published a follow-up novel in 2015, Go Set A Watchman, which is set in the 1950s and shows the progression of the characters two decades on. It not only confirms the brilliance of To Kill A Mockingbird, but adds new context and meaning to the classic."},
    {"id": 3, "title": "Wuthering Heights", "author": "Emily Brontë", "img_link": "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1689758274-screenshot-2023-07-19-at-10-17-34-64b7aa33ba35c.png?crop=0.9752198241406875xw:1xh;center,top&resize=980:*", "description": "No reading list would be complete without Emily Brontë's gothic romance, Wuthering Heights. Written in 1847 as a reaction to the popular romantic fiction of Jane Austen, it is an altogether darker and more complicated tale, set within a frame narrative and spanning two generations. Featuring some of the most beautiful prose in the English canon, it describes the destructive relationship between Catherine Earnshaw and Heathcliff, a foundling, amid the wild and feral atmosphere of the Yorkshire moors. Emily Brontë's sole published work, this evokes the violence of doomed romance and the creeping darkness of vengeance like no other novel."},
    {"id": 4, "title": "1984", "author": "George Orwell", "img_link": "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1689759599-screenshot-2023-07-19-at-10-39-39-64b7af638c17e.png?crop=0.9878345498783455xw:1xh;center,top&resize=980:*", "description": 'Perhaps the most brilliant ever dystopian depiction of a totalitarian society, 1984 is as much a historical and cultural polemic as it is an absorbing thriller. Words from the novel have permeated our commonplace lexicon (\'doublethink\' and \'Big Brother\' among them) and the book continues to be influential today. As the critic and author Jonathan Freedland wrote about 1984, \'it has become a shorthand for... the surveillance state, for the power of the mass media to manipulate public opinion, history and even the truth\'. A book that encompasses freedom, betrayal and the power of protest, it\'s a cornerstone of British literature.'},
    {"id": 5, "title": "Pride and Prejudice", "author": "Jane Austen", "img_link": "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1704985218-screenshot-2024-01-11-at-14-59-51-65a00270623e0.png?crop=0.993431855500821xw:1xh;center,top&resize=980:*", "description": "Austen’s most famous novel – and arguably one of the most famous ever written in the English language – manages to be at once witty, wry, modern and timeless. Focused on the courtship of Elizabeth Bennet (one of the great feminist heroes of literature) and Fitzwilliam Darcy, this is much more than just a traditional love story, and is chock-full of laugh-out-loud characters, playfulness and irony. A great introduction to Austen, if you like this, we'd recommend Persuasion, another classic featuring a strong heroine."},
    {"id": 6, "title": "Mrs Dalloway", "author": "Virginia Woolf", "img_link": "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1714047049-81uR-LIhJS.jpg?crop=1xw:0.926xh;center,top&resize=980:*", "description": "On a perfect June morning, Clarissa Dalloway – fashionable, worldly, wealthy and an accomplished hostess – sets off to buy flowers for the party she will host that evening. During her journey, she is preoccupied with thoughts of the present and memories of the past, and from her interior monologue emerge the people who have touched her life. Bold and experimental, Virginia Woolf's Mrs Dalloway is a landmark twentieth-century work of fiction, a genuine innovation in the history of novel writing – and an excellent, transporting read."},
    {"id": 7, "title": "Great Expectations", "author": "Charles Dickens", "img_link": "https://m.media-amazon.com/images/I/51evTcoKMGL.jpg", "description": "When Charles Dickens wrote Great Expectations, he gave life to some of literature’s most colorful and enduring characters: Pip, Miss Havisham, and Uncle Pumblechook, to name a few. His penultimate novel, Great Expectations details the life and stories of an orphan named Pip, growing up in Kent and London in the early to mid-1800s. It’s a classic and a must-read quite simply because it’s been described as one of Dickens’ best works, an appraisal to which Dickens himself agreed."},
    {"id": 8, "title": "And Then There Were None", "author": "Agatha Christie", "img_link": "https://prodimage.images-bn.com/pimages/9780062073471_p0_v9_s1200x630.jpg", "description": "In a world rife with paperback mysteries and e-books, Agatha Christie remains one of the most popular, well-known mystery writers of all time. In her vast collection, And Then There Were None frequently rises to the top. It’s a classic whodunit. Ten strangers are invited to a remote mansion on a desolate island. Once they’ve arrived, each guest is accused of murder. So what really happened? And who is responsible? Pick up a copy to find out; it makes a great summer read, after all."},
    {"id": 9, "title": "The Book Thief", "author": "Markus Zusak", "img_link": "https://m.media-amazon.com/images/I/914cHl9v7oL._AC_UF1000,1000_QL80_.jpg", "description": "If you’re reading this list, you likely understand the power that a book has to feed and nurture a soul. In that case, Markus Zusak’s The Book Thief will be right at home in your hands. In 1939 Nazi Germany, Liesel Meminger seeks meaning and life amid the bombings and death. Her “weapon” of choice? Books and the written word. This is a beautiful, riveting tale that helped make the horrors of World War II fresh again for readers who learned about it from history books. "},
    {"id": 10, "title": "The Stranger", "author": "Albert Camus", "img_link": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1590930002i/49552.jpg", "description": "Albert Camus’ The Stranger has long lived a dual life of meaning: In one way, it’s a story of mystery, murder, death, and destruction. In another, it’s a sermon on the absurd and the power of human thought. Camus, for his part, wrote, “I summarized The Stranger a long time ago with a remark I admit was highly paradoxical: ‘In our society, any man who does not weep at his mother’s funeral runs the risk of being sentenced to death.’ I only meant that the hero of my book is condemned because he does not play the game.”"},
]


def homepage(request):
    return render(request, 'index.html', {'books': books})


def book_details(request, book_id):

    details = None

    for book in books:
        if book['id'] == book_id:
            details = book
            break

    return render(request, 'book_details.html', {"details": details})


def delete_book(request, book_id):

    book_to_delete = None

    for book in books:
        if book['id'] == book_id:
            book_to_delete = book
            break

    books.remove(book_to_delete)

    return redirect('books:homepage')


