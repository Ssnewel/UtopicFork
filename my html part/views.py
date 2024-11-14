def add_publication(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        if name and text:
            publication = Publication.objects.create(
                user=request.user, name=name, text=text
            )
            return redirect('publication_detail', publication_id=publication.id)
    return render(request, 'add_publication.html')

# Добавление комментария к публикации
@login_required
def add_comment(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(
                user=request.user, publication=publication, text=text
            )
            return redirect('publication_detail', publication_id=publication.id)
    return render(request, 'add_comment.html', {'publication': publication})

# "Мягкое" удаление публикации
@login_required
def delete_publication(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id, user=request.user)
    publication.deleted_at = timezone.now()
    publication.save()
    return JsonResponse({'status': 'Publication deleted'})

# "Мягкое" удаление комментария
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    comment.deleted_at = timezone.now()
    comment.save()
    return JsonResponse({'status': 'Comment deleted'})

@login_required
def add_attachment_to_publication(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    if request.method == 'POST' and request.FILES.get('attachment'):
        attachment_file = request.FILES['attachment']
        attachment = Attachment.objects.create(file=attachment_file, user=request.user)
        publication.attachments.add(attachment)
        return redirect('publication_detail', publication_id=publication.id)
    return render(request, 'add_attachment.html', {'publication': publication})
