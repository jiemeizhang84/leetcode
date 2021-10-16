class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = collections.Counter()
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            subdomain = domain.split('.')
            for i in range(len(subdomain)):
                cnt['.'.join(subdomain[i:])] += count
        return [f'{value} {key}' for key, value in cnt.items()]