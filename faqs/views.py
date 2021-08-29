from django.shortcuts import render


def frequent_questions(request):
    """ A view to return the FAQs page """

    return render(request, 'faqs/frequent_questions.html')
