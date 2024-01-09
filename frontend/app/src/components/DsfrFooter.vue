<script setup lang="ts">
import { reactive, watch } from 'vue'
import { DsfrFooter } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		beforeMandatoryLinks?: Array<any>
		afterMandatoryLinks?: Array<any>
		a11yCompliance?: 'non conforme' | 'partiellement conforme' | 'totalement conforme'
		logoText?: string | string[]
		legalLink?: string
		personalDataLink?: string
		cookiesLink?: string
		a11yComplianceLink?: string
		descText?: string
		homeLink?: string
		licenceText?: string
		licenceTo?: string
		licenceName?: string
		licenceLinkProps?: any
		ecosystemLinks?: Array<any>
		partners?: any
		mandatoryLinks?: Array<any>
		operatorLinkText?: string
		operatorTo?: string
		operatorImgStyle?: any
		operatorImgSrc?: string
		operatorImgAlt?: string
	}>
>()
</script>

<template>
	<div class="component">
		<DsfrFooter
			:beforeMandatoryLinks="props.args.beforeMandatoryLinks"
			:afterMandatoryLinks="props.args.afterMandatoryLinks"
			:a11yCompliance="props.args.a11yCompliance"
			:logoText="props.args.logoText"
			:legalLink="props.args.legalLink"
			:personalDataLink="props.args.personalDataLink"
			:cookiesLink="props.args.cookiesLink"
			:a11yComplianceLink="props.args.a11yComplianceLink"
			:descText="props.args.descText"
			:homeLink="props.args.homeLink"
			:licenceText="props.args.licenceText"
			:licenceTo="props.args.licenceTo"
			:licenceName="props.args.licenceName"
			:licenceLinkProps="props.args.licenceLinkProps"
			:ecosystemLinks="props.args.ecosystemLinks"
			:partners="props.args.partners"
			:mandatoryLinks="props.args.mandatoryLinks"
			:operatorLinkText="props.args.operatorLinkText"
			:operatorTo="props.args.operatorTo"
			:operatorImgStyle="props.args.operatorImgStyle"
			:operatorImgSrc="props.args.operatorImgSrc"
			:operatorImgAlt="props.args.operatorImgAlt"
		/>
	</div>
</template>
